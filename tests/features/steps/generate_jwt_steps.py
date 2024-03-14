import os
from behave import *
from src.generate_key_pair import generate_key_pair, PRIVATE_KEY_FILENAME
from src.encode_jwt import encode_jwt, JWT_FILENAME

use_step_matcher("re")


@when("I attempt to create a JWT using a private key")
def step_impl(context):
    try:
        encode_jwt()
    except Exception:
        pass


@then("I see that the JWT has been created successfully")
def step_impl(context):
    assert os.path.isfile(JWT_FILENAME)


@given("No JWT file exists")
def step_impl(context):
    if os.path.isfile(JWT_FILENAME):
        os.remove(JWT_FILENAME)


@then("I see that no JWT has been created")
def step_impl(context):
    assert not os.path.isfile(JWT_FILENAME)


@given("No private keys exist")
def step_impl(context):
    if os.path.isfile(PRIVATE_KEY_FILENAME):
        os.remove(PRIVATE_KEY_FILENAME)


@given("A private key exists")
def step_impl(context):
    if not os.path.isfile(PRIVATE_KEY_FILENAME):
        generate_key_pair()
