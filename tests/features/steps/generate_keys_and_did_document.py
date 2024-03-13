import os
from behave import *
from src.generate_key_pair import generate_key_pair
from src.generate_did import generate_did_web

use_step_matcher("re")


@when("I generate a private/public keypair")
def step_impl(context):
    generate_key_pair()


@then("I see that a file is generated for both a private and public key")
def step_impl(context):
    assert os.path.isfile('private_key.pem')
    assert os.path.isfile('public_key.pem')


@when("I generate a did:web document from the saved keypair")
def step_impl(context):
    generate_did_web()


@then("I see that a file is generated containing the did:web document")
def step_impl(context):
    assert os.path.isfile('did.json')
