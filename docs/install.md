# Installation
This project uses [Poetry](https://python-poetry.org/) for dependency management.

You can use the following method to replace the PyPI mirror source, default is tsinghua mirror:

```bash
poetry source add --priority=default mirrors https://pypi.tuna.tsinghua.edu.cn/simple/
```

Then, install the dependencies:

```bash
poetry install
```

activate the virtual environment:

```bash
poetry shell
```

install the pre-commit hooks:

```bash
pre-commit install
```

# Environment
You need to create a `.env` file in the root directory of the project, and fill in the following environment variables:

* OPENAI_API_KEY=
* OPENAI_API_BASE=https://api.openai.com/v1 (optional)
* OPENAI_PROXY= (optional) # 访问受限的情况下，可以使用代理

```bash
cp .env.example .env
```
