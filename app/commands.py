# -*- coding: utf-8 -*-
import json
import os

import click

from app.models.host import Host
from app.models.job import Job
from app.models.predictor import Predictor
from app.models.repacs import RePACS
from app.models.servlet import Servlet
from app.models.worker import Worker


def init_job(db, job, repacs, predictor, servlets):
    job.repacs = repacs
    job.predictor = predictor
    job.servlets = servlets
    db.session.add(job)


def forge_cmd(db, count):
    db.drop_all()
    db.create_all()

    click.echo("Generating workers...")
    for i in range(count):
        worker = Worker(id=i, gpu=i, default_job="ct1mm")
        db.session.add(worker)

    click.echo("Generating RePACS...")
    host_ip = os.getenv("HOST_IP", "localhost")
    click.echo(f"Generating repacs... host_ip={host_ip}")
    repacs = RePACS(id=0, host=host_ip, port=3333)
    db.session.add(repacs)

    click.echo("Generating Hosts...")
    h0 = Host(id=0, host=host_ip, gpus="0,1,2,3")
    db.session.add(h0)
    h1 = Host(id=1, host="192.168.111.246", gpus="0")
    db.session.add(h1)

    click.echo("Generating predictor...")
    predictor = Predictor(id=0, name="ct1mm", version="2.0", shared_memory_name="ct1mm")
    db.session.add(predictor)

    click.echo(f"Generating servlet... HOST_IP={host_ip}")
    servlets = []
    servlet1 = Servlet(
        id=0,
        name="ct1mm",
        service_type="detect",
        grpc_host=host_ip,
        grpc_port=1235,
        mandatory=True,
    )
    servlets.append(servlet1)
    servlet2 = Servlet(
        id=1,
        name="ct1mm",
        service_type="imgsearch",
        grpc_host=host_ip,
        grpc_port=1235,
        mandatory=False,
    )
    servlets.append(servlet2)

    init_job(
        db,
        Job(id=0, name="ct1mm", task_type="predict/ct_lung"),
        repacs,
        predictor,
        servlets,
    )

    #
    # ct 5 mm
    #

    predictor = Predictor(id=1, name="ct5mm", version="1.0", shared_memory_name="ct5mm")
    servlets = []
    servlet1 = Servlet(
        id=2,
        name="ct5mm",
        service_type="detect",
        grpc_host=host_ip,
        grpc_port=1236,
        mandatory=True,
    )
    servlets.append(servlet1)
    init_job(
        db,
        Job(id=1, name="ct5mm", task_type="predict/ct_lung:5mm"),
        repacs,
        predictor,
        servlets,
    )

    #
    # ct fracture
    #
    recon = {
        "recon_image_size": os.getenv("RECON_IMAGE_SIZE", 512),
        "recon_image_angle": os.getenv("RECON_IMAGE_ANGLE", 360),
        "recon_image_number": os.getenv("RECON_IMAGE_NUMBER", 18),
        "storage_vr1_host": os.getenv("STORAGE_VR1_HOST", "fs1"),
        "storage_vr1_root": os.getenv("STORAGE_VR1_ROOT", "/media/tx-deepocean/Data/"),
    }
    predictor = Predictor(
        id=2,
        name="fracture",
        version="1.0",
        shared_memory_name="fracture",
        recon=json.dumps(recon),
    )
    servlets = []
    servlet1 = Servlet(
        id=3,
        name="fracture",
        service_type="detect",
        grpc_host=host_ip,
        grpc_port=2435,
        mandatory=True,
    )
    servlets.append(servlet1)
    servlet2 = Servlet(
        id=4,
        name="fracture",
        service_type="bonevr",
        grpc_host=host_ip,
        grpc_port=9876,
        mandatory=True,
    )
    servlets.append(servlet2)
    init_job(
        db,
        Job(id=2, name="ct5mm", task_type="predict/ct_chest_fracture"),
        repacs,
        predictor,
        servlets,
    )

    db.session.commit()
    click.echo("Created %d workers." % count)
