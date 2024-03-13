Feature: Part 3 - Create JWT from private key
    As an administrator
    I want to create a JWT from a private key
    So I can secure my communications

    Background:
        Given No JWT file exists

    Scenario: I am unable to create a JWT if a private key does not exist
        Given No private keys exist
        When I attempt to create a JWT using a private key
        Then I see that no JWT has been created

    Scenario: I can create a JWT using a private key
        Given A private key exists
        When I attempt to create a JWT using a private key
        Then I see that the JWT has been created successfully
