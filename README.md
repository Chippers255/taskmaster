# TaskMaster

[![GitHub License](https://img.shields.io/github/license/Chippers255/taskmaster)](https://github.com/Chippers255/taskmaster/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/Chippers255/taskmaster)](https://github.com/Chippers255/taskmaster/issues)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Chippers255/taskmaster/python-package.yml?branch=main)](https://github.com/Chippers255/taskmaster/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/Chippers255/taskmaster/branch/main/graph/badge.svg?token=FF6K13JPUL)](https://codecov.io/gh/Chippers255/taskmaster)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

An GPT powered task management system inspired by [babyagi](https://github.com/yoheinakajima/babyagi).

## How to Use

### Install
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install .
```

### Run
```bash
export PINECONE_API_KEY=<YOUR PINECONE API KEY GOES HERE>
export OPENAI_API_KEY=<YOUR OPENAI API KEY GOES HERE>
python main.py
```
