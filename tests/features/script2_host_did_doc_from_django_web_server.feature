Feature: Script 2 - Host DID document on django webserver
    As an administrator
    I want to retrieve a hosted DID document
    So I can use its public key

    Scenario: A django webserver is running
        When I startup the local django webserver
        Then I can navigate to the root index page

#    Scenario: A django webserver is running
#        Given I startup the local django webserver
#        When I attempt to retrieve a DID:WEB document
#        Then I receive the contents of the DID:WEB document
