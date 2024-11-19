# Test Case Design for Grocery Mate Webshop

## Testing Strategies Summary

- **Boundary Value Analysis (BVA)**: Used for input limits.
- **State Transition Testing**: Applied to validate transitions between states, such as registration status and payment states.
- **Equivalence Partitioning (EP)**: Utilized for valid/invalid input classifications and browser support.
- **Error Guessing**: Focused on unexpected user behaviors.
- **Decision Table Testing**: Ensures all possible conditions are accounted for in payment transitions.

---

## Highlighted Feature: Product Search

| Test ID             | Objective                                                                                      | Expected Result                                                                                 | Actual Result | Pass/Fail |
|----------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Product Search-01** | Verify that users can search for products using the search bar with valid input.               | A list of matching products is displayed.                                                      |               |           |
| **Product Search-02** | Verify that the system shows an error message for invalid or nonsensical input.               | "No products found" message is displayed.                                                      |               |           |
| **Product Search-03** | Verify case-insensitive search functionality.                                                  | Search results are displayed regardless of case.                                                |               |           |
| **Product Search-04** | Verify search with special characters and symbols in the query.                               | Appropriate error handling or empty results returned.                                           |               |           |
| **Product Search-05** | Verify that search results are sorted correctly (e.g., by relevance or alphabetical order).    | Results appear in the defined order.                                                           |               |           |
| **Product Search-06** | Verify search with no results due to a typo and suggest possible corrections (if applicable).  | The system offers a "Did you mean?" suggestion (if implemented).                                |               |           |

---

## Boundary Value Analysis (BVA)

| Test ID             | Objective                                                                                      | Expected Result                                                                                 | Actual Result | Pass/Fail |
|----------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **BVA-01**           | Verify registration fails when entering a username with less than 3 characters.               | Error message: "Username must be at least 3 characters long."                                   |               |           |
| **BVA-02**           | Verify registration fails when entering a password shorter than 6 characters.                 | Error message: "Password must be at least 6 characters long."                                   |               |           |
| **BVA-03**           | Verify product search returns results with the maximum allowed characters.                    | System displays products matching the search criteria.                                          |               |           |
| **BVA-04**           | Verify product search returns no results with zero characters.                                | System shows an error message: "Search query cannot be empty."                                  |               |           |

---

## State Transition Testing

| Test ID             | Objective                                                                                      | Expected Result                                                                                 | Actual Result | Pass/Fail |
|----------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **StateTransition-01** | Verify user registration process transitions from "unregistered" to "registered".              | User successfully registers and transitions to the registered state.                            |               |           |
| **StateTransition-02** | Verify payment transitions from "pending" to "completed" upon successful transaction.          | Payment status updates to "completed" after a successful transaction.                           |               |           |
| **StateTransition-03** | Verify payment transitions from "pending" to "failed" upon unsuccessful transaction.          | Payment status updates to "failed" after an unsuccessful transaction.                           |               |           |

---

## Decision Table Testing for Payment Status Transitions

| Condition               | Payment Details Provided | Payment Validated | Payment Processed | Result       |
|--------------------------|--------------------------|-------------------|-------------------|--------------|
| Valid payment info       | Yes                      | Yes               | Yes               | Success      |
| Missing payment info     | No                       | -                 | -                 | Failure      |
| Invalid payment info     | Yes                      | No                | -                 | Failure      |
| Error during processing  | Yes                      | Yes               | No                | Failure      |

---

## Additional Test Cases

### User Registration Tests

| Test ID             | Objective                                                                                      | Expected Result                                                                                 | Actual Result | Pass/Fail |
|----------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Registration-01**  | Verify that a user can successfully register with valid information.                          | User receives a confirmation message and is redirected to the login page.                       |               |           |
| **Registration-02**  | Verify that registration fails with an already existing username.                             | Error message: "Username already exists."                                                      |               |           |

---

### Accessibility Tests

| Test ID             | Objective                                                                                      | Expected Result                                                                                 | Actual Result | Pass/Fail |
|----------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Accessibility-01** | Verify that the website is navigable using keyboard-only controls.                             | All links and buttons are accessible without a mouse.                                           |               |           |
| **Accessibility-02** | Verify that all images have descriptive alt text for screen readers.                           | Screen reader announces images correctly with their descriptions.                               |               |           |
| **Accessibility-03** | Verify that color contrast meets accessibility standards.                                      | All text elements meet or exceed the required contrast ratio for readability.                   |               |           |

---

### Browser Compatibility Tests

| Test ID             | Objective                                                                                      | Expected Result                                                                                 | Actual Result | Pass/Fail |
|----------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Browser-01**       | Verify website functionality on Chrome.                                                       | All features work correctly on the Chrome browser.                                              |               |           |
| **Browser-02**       | Verify website functionality on Firefox.                                                      | All features work correctly on the Firefox browser.                                             |               |           |
| **Browser-03**       | Verify website functionality on Safari.                                                       | All features work correctly on the Safari browser.                                              |               |           |
| **Browser-04**       | Verify website functionality on Edge.                                                         | All features work correctly on the Edge browser.                                                |               |           |

---