#!/usr/bin/env python3

from aws_cdk import core

from static_site_stack.static_site_stack import StaticSiteStack

app = core.App()

env = app.node.try_get_context("environment")
domain = app.node.try_get_context("domain")

stack_id = f"StaticSiteStack-{env}"
StaticSiteStack(app, stack_id, env, domain)

app.synth()
