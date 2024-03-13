Feature: Part 3 - Create JWT from private key
    As an administrator
    I want to create a JWT from a private key
    So I can secure my communications

    Scenario: I can create a JWT using a private key
        When I attempt to create a JWT using a private key
        Then I see that the JWT has been created successfully
