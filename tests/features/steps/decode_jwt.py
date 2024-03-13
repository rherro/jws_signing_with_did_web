from behave import *
from src.create_jwt import decode_jwt
from src.generate_key_pair import generate_key_pair
from src.generate_did import generate_did_web
from src.create_jwt import create_jwt, PAYLOAD

use_step_matcher("re")


@given("I generate new dependency files")
def step_impl(context):
    generate_key_pair()
    generate_did_web()
    create_jwt()


@when("I decode a JWT")
def step_impl(context):
    context.result = decode_jwt()


@then("I see that the payload of the message matches the original payload")
def step_impl(context):
    assert 'result' in context
    assert context.result == PAYLOAD
