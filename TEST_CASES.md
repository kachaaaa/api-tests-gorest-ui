# Test Cases — api-tests-gorest-ui

| ID  | Feature | Test Case Description | Pre-conditions | Test Steps | Test Data | Expected Result | Status |
|-----|---------|--------------------|----------------|------------|-----------|----------------|--------|
| TC01 | GET /users | Get list of users | API is available, valid token | Send GET request to /users | N/A | Status 200, response is list of users | Pass |
| TC02 | GET /users/{id} | Get user by valid ID | User exists | Send GET request to /users/{id} | Valid user ID | Status 200, response contains correct user data | Pass |
| TC03 | GET /users/{id} | Get user by invalid ID | API is available | Send GET request to /users/{id} | Non-existing ID | Status 404, response contains error message | Pass |
| TC04 | POST /users | Create user with valid data | API is available, valid token | Send POST request to /users | Name, email, gender, status | Status 201, response contains created user | Pass |
| TC05 | POST /users | Create user with empty body | API is available, valid token | Send POST request with empty JSON | N/A | Status 422, validation error in response | Pass |
| TC06 | POST /users | Create user with invalid email | API is available, valid token | Send POST request with invalid email | Name, "bad-email" | Status 422, validation error | Pass |
| TC07 | POST /users | Create user without required fields | API is available, valid token | Send POST request without name/email | Empty JSON | Status 422, validation error | Pass |
| TC08 | DELETE /users/{id} | Delete existing user | User exists | Send DELETE request to /users/{id} | Valid user ID | Status 204, user is deleted | Pass |
| TC09 | DELETE /users/{id} | Delete non-existing user | API is available | Send DELETE request to /users/{id} | Non-existing ID | Status 404, response contains error message | Pass |