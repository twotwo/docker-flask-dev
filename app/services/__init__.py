# -*- coding: utf-8 -*-
import json

from flask import current_app

from app.models.host import Host
from app.models.job import Job, job_schema, job_schemas
from app.models.repacs import RePACS
from app.models.servlet import Servlet


class JobHandler(object):
    @staticmethod
    def get_all():
        jobs = Job.query.all()
        return job_schemas.dump(jobs)

    @staticmethod
    def get_job(host: int, gpu: int):
        """Get Job by Host.GPU

        """
        config = current_app.app_config
        current_host_ip = config.get("hosts").get(host).get("ip")
        default_job = (
            config.get("hosts").get(host).get("gpus").get(gpu).get("default_job")
        )
        return JobHandler.render_host_ip(
            config.get("jobs").get(default_job), current_host_ip
        )

    @staticmethod
    def render_host_ip(resp: dict, host_ip):
        res = json.dumps(resp).replace("${HOST_IP}", host_ip)
        return json.loads(res)

    @staticmethod
    def get_job_by_gpu(gpu: int):
        """Get job by gpu.
        """
        job = Job.query.get(gpu)
        if job.predictor.shared_memory_name:
            job.predictor.shared_memory_name = (
                f"{job.predictor.shared_memory_name}_gpu{gpu}"
            )
        return job_schema.dump(job) if job else {}
        # return Job.share_schema.dump(job) if job else {}


class ConfigInfo(object):
    """Load basic Config Info for render
    """

    @staticmethod
    def get_all():
        configs = {}
        repacsAll = RePACS.query.all()
        configs["RePACSs"] = repacsAll
        configs["Hosts"] = Host.query.all()
        configs["Servlets"] = Servlet.query.all()
        return configs
