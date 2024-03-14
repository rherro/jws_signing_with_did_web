import os
from behave import *
from generate_key_pair import generate_key_pair, PRIVATE_KEY_FILENAME
from generate_did import generate_did_web, DID_WEB_FILENAME
from encode_jwt import encode_jwt, PAYLOAD
from decode_jwt import decode_jwt

use_step_matcher("re")


@given("I generate new dependency files")
def step_impl(context):
    generate_key_pair()
    generate_did_web()
    encode_jwt()


@when("I decode a JWT")
def step_impl(context):
    try:
        context.decoded_jwt = decode_jwt()
    except Exception:
        pass


@then("I see that the payload of the message matches the original payload")
def step_impl(context):
    assert 'decoded_jwt' in context
    assert context.decoded_jwt == PAYLOAD


@given("No dependency files exist")
def step_impl(context):
    if os.path.exists(DID_WEB_FILENAME):
        os.remove(DID_WEB_FILENAME)

    if os.path.isfile(PRIVATE_KEY_FILENAME):
        os.remove(PRIVATE_KEY_FILENAME)


@then("I am unable to extract the original payload")
def step_impl(context):
    assert 'result' not in context
