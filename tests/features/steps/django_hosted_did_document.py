from behave import *
import urllib.request

use_step_matcher("re")

BASE_URL = 'http://localhost:8000'
DID_WEB_URL = f'{BASE_URL}/.well_known/did.json'


@step("I startup the local django webserver")
def step_impl(context):
    # This will be a manual process for right now
    pass


@then("I can navigate to the root index page")
def step_impl(context):
    contents = urllib.request.urlopen(BASE_URL).read()
    assert contents


@when("I attempt to retrieve a DID:WEB document")
def step_impl(context):
    context.did_web_document = urllib.request.urlopen(DID_WEB_URL).read()


@then("I receive the contents of the DID:WEB document")
def step_impl(context):
    assert context.did_web_document is not None
