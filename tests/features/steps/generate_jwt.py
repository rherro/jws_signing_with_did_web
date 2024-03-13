from behave import *
from src.create_jwt import create_jwt

use_step_matcher("re")


@when("I attempt to create a JWT using a private key")
def step_impl(context):
    context.jwt = create_jwt()
    pass


@then("I see that the JWT has been created successfully")
def step_impl(context):
    assert 'jwt' in context
    assert context.jwt is not None
