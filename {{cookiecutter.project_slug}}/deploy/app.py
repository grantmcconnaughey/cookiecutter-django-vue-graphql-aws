#!/usr/bin/env python3

from aws_cdk import core

from {{cookiecutter.project_slug}}.frontend import FrontendStack
from {{cookiecutter.project_slug}}.networking import NetworkingAndDBStack

app = core.App()
FrontendStack(app, "{{cookiecutter.project_slug}}-frontend")
NetworkingAndDBStack(app, "{{cookiecutter.project_slug}}-networking-db")

app.synth()
