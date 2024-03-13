Feature: Part 4 - Decode JWT
    As an administrator
    I want to decode a JWT using the public key from a DID:WEB document
    So I can retrieve and validate my communications

    Scenario: I am unable to decode a JWT if no dependency files exist
        Given No dependency files exist
        When I decode a JWT
        Then I am unable to extract the original payload

    Scenario: I can decode a JWT using a DID:WEB document
        Given I generate new dependency files
        When I decode a JWT
        Then I see that the payload of the message matches the original payload
