import pytest

from app.models.job import Job
from app.models.predictor import Predictor
from app.models.repacs import RePACS
from app.models.servlet import Servlet
from app.models.worker import Worker


@pytest.fixture
def worker():
    return Worker(gpu=0, default_job="ct1mm")


@pytest.fixture
def repacs():
    return RePACS(host="localhost", port=3333)


@pytest.fixture
def predictor():
    return Predictor(name="ct1mm", version="1.0", shared_memory_name="ct1mm")


@pytest.fixture
def servlet():
    return Servlet(name="ct1mm", service_type="", grpc_host="localhost", grpc_port=1235)


@pytest.fixture
def job(repacs, predictor, servlet):
    j = Job(task_type="predict/ct_lung")
    j.repacs = repacs
    j.predictor = predictor
    j.servlets = [servlet]
    return j
