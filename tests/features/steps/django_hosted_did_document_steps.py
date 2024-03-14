import os
from behave import *
import urllib.request
import urllib.error
from generate_keys_and_did_document_steps import generate_did_web, DID_WEB_FILENAME

use_step_matcher("re")

BASE_URL = 'http://localhost:8000'
DID_WEB_URL = f'{BASE_URL}/.well-known/did.json'


@step("I startup the local django webserver")
def step_impl(context):
    # This will be a manual process for right now
    pass


@when("I attempt to retrieve a DID:WEB document")
def step_impl(context):
    try:
        context.did_web_document = urllib.request.urlopen(DID_WEB_URL).read()
    except Exception as e:
        context.error = e


@then("I receive the contents of the DID:WEB document")
def step_impl(context):
    assert context.did_web_document is not None


@step("no DID:WEB document exists")
def step_impl(context):
    if os.path.exists(DID_WEB_FILENAME):
        os.remove(DID_WEB_FILENAME)


@step("a DID:WEB document exists")
def step_impl(context):
    if not os.path.exists(DID_WEB_FILENAME):
        generate_did_web()


@then('I receive a "404 Not Found error"')
def step_impl(context):
    assert 'error' in context
    assert isinstance(context.error, urllib.error.HTTPError)
    assert context.error.code == 404
