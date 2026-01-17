# Test Plan — api-tests-gorest-ui

## 1. Introduction
This Test Plan describes the testing approach, scope, and objectives
for the **api-tests-gorest-ui** project.

The project focuses on automated testing of the GoRest Users REST API
as a backend layer for future UI testing.

The purpose of testing is to validate correctness, reliability,
and error handling of the API endpoints used by the UI layer.

---

## 2. Scope of Testing

### In Scope
- GoRest Users API
- CRUD operations:
  - GET users
  - GET user by ID
  - POST create user
  - DELETE user
- Automated API tests
- Positive and negative scenarios
- HTTP status code validation
- Response body validation

### Out of Scope
- UI automation (will be added later)
- Performance / load testing
- Security testing
- PUT / PATCH operations

---

## 3. Test Types
- Automated API testing
- Functional testing
- Positive testing
- Negative testing

---

## 4. Test Environment
- API: GoRest Public API
- Base URL: https://gorest.co.in/public/v2
- Authorization: Bearer Token
- Test framework: pytest
- Programming language: Python
- HTTP client: requests

---

## 5. Test Tools
- Python 3
- pytest
- requests
- PyCharm
- GitHub

---

## 6. Test Scenarios

### GET
- Retrieve users list
- Retrieve user by valid ID
- Retrieve user by invalid ID (404)

### POST
- Create user with valid data (201)
- Create user with empty request body (422)
- Create user with invalid email (422)
- Create user without required fields (422)

### DELETE
- Delete existing user (204)
- Delete non-existing user (404)

---

## 7. Entry Criteria
- API is available
- Valid API token is configured
- Test environment is ready

---

## 8. Exit Criteria
- All planned tests are executed
- All critical defects are resolved or documented
- No blocking issues remain

---

## 9. Risks
- API rate limits
- Dependency on external public API
- Test data conflicts
- Network issues

---

## 10. Deliverables
- Automated API test scripts
- Test execution results
- README documentation
- Test Plan document