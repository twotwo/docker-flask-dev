# -*- coding: utf-8 -*-
from app.models.job import Job


def test_create_job(db):
    job = Job.create(name="ct1mm", task_type="predict/ct_lung")
    assert Job.query.count() == 1
    assert Job.query.first() == job


def test_save_job(db, job, repacs):
    job.save(commit=True)
    _job = Job.query.get(1)
    assert Job.query.count() == 1
    assert Job.query.first() == job
    assert _job == job
    assert _job.id == 1
    assert _job.repacs == repacs


def test_delete_job(db, job):
    job.save(commit=True)
    assert job.query.count() == 1
    _job = job.query.get(1)
    _job.delete(commit=True)
    assert job.query.count() == 0


def test_update_job(db, job):
    job.save(commit=True)
    assert job.query.count() == 1
    _job = job.query.get(1)
    _job.name = "ct5mm"
    _job.task_type = "predict/ct_lung:ct5mm"
    _job.save(commit=True)
    assert Job.query.count() == 1
    _job_mod = job.query.get(1)
    assert _job_mod.name == "ct5mm"
    assert _job_mod.task_type == "predict/ct_lung:ct5mm"
    _job.update(name="fracture", task_type="predict/ct_chest_fracture")
    _job.save(commit=True)
    assert Job.query.count() == 1
    _job_mod = job.query.get(1)
    assert _job_mod.name == "fracture"
    assert _job_mod.task_type == "predict/ct_chest_fracture"
