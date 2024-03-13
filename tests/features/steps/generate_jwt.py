import os
from behave import *
from src.generate_key_pair import generate_key_pair
from src.create_jwt import create_jwt

use_step_matcher("re")


@when("I attempt to create a JWT using a private key")
def step_impl(context):
    try:
        create_jwt()
    except Exception:
        pass


@then("I see that the JWT has been created successfully")
def step_impl(context):
    assert os.path.isfile('jwt')


@given("No JWT file exists")
def step_impl(context):
    if os.path.isfile('jwt'):
        os.remove('jwt')


@then("I see that no JWT has been created")
def step_impl(context):
    assert not os.path.isfile('jwt')


@given("No private keys exist")
def step_impl(context):
    if os.path.isfile('private_key.pem'):
        os.remove('private_key.pem')


@given("A private key exists")
def step_impl(context):
    if not os.path.isfile('private_key.pem'):
        generate_key_pair()
