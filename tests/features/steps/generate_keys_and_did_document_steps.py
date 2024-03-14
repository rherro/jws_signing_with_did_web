import os
from behave import *
from src.generate_key_pair import generate_key_pair, PRIVATE_KEY_FILENAME, PUBLIC_KEY_FILENAME
from src.generate_did import generate_did_web, DID_WEB_FILENAME

use_step_matcher("re")


@when("I generate a private/public keypair")
def step_impl(context):
    generate_key_pair()


@then("I see that a file is generated for both a private and public key")
def step_impl(context):
    assert os.path.isfile(PRIVATE_KEY_FILENAME)
    assert os.path.isfile(PUBLIC_KEY_FILENAME)


@when("I generate a did:web document from the saved keypair")
def step_impl(context):
    generate_did_web()


@then("I see that a file is generated containing the did:web document")
def step_impl(context):
    assert os.path.isfile(DID_WEB_FILENAME)
