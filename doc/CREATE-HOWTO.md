# How to Create a modern flask Project

## init flask project

### installation

    python -m pip install --user pipx
    python -m pipx ensurepath
    pipx install pipenv -i https://mirrors.aliyun.com/pypi/simple
    pipenv install --dev
    pipenv run pre-commit install --install-hooks
    # Run hooks
    pipenv run pre-commit run

### vs code integration

    # 选择 pipenv 环境
    Cmd+Shilf+P >Python: Select Interpreter

    # 集成 pytest
    Cmd+Shilf+P >Python:Discover Tests

### run flask project

    # 运行测试，并使用 pytest-cov 获得测试覆盖率
    pipenv run pytest --cov --cov-fail-under=80
    # 初始化服务配置
    pipenv run flask forge
    # 启动服务
    pipenv run flask run
    # 访问 http://localhost:8080/apidocs
    # run by docker
    docker build -t flask-dev .
    docker run --name flask-dev -p 8080:8080 -d flask-dev

## 重要配置说明

### Pipfile.dev-packages

    pipenv install --dev
    # isort 按字母顺序对 import 进行排序
    # black 代码格式化工具
    # flake8 格式检查
    # mypy 静态类型检查
    # pytest pytest-cov 单元测试和测试覆盖率统计
    # pre-commit 管理多种语言的 pre-commit hooks

### setup.cfg

[Writing the Setup Configuration File](https://docs.python.org/3.7/distutils/configfile.html)

### .pre-commit-config.yaml

https://pre-commit.com/