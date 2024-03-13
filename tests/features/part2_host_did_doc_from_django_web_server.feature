Feature: Part 2 - Host DID document on django webserver
    As an administrator
    I want to retrieve a hosted DID document
    So I can use its public key

    Scenario: I receive an error when attempting to retrieve the DID:WEB document before it's created
        Given I startup the local django webserver
        And no DID:WEB document exists
        When I attempt to retrieve a DID:WEB document
        Then I receive a "404 Not Found error"

    Scenario: I am able to retrieve a hosted DID:WEB document
        Given I startup the local django webserver
        And a DID:WEB document exists
        When I attempt to retrieve a DID:WEB document
        Then I receive the contents of the DID:WEB document
