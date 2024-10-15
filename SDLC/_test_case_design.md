# Test Case Design for Grocery Mate Webshop

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **User Registration - TC-01**     | Verify that a user can successfully register with valid information.       | User receives a confirmation message and is redirected to the login page.                       |               |           |
| **User Registration - TC-02**     | Verify that registration fails with an already existing username.          | An error message is displayed indicating that the username already exists.                      |               |           |

### Product Search Tests

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Product Search - TC-01**        | Verify that users can search for products using the search bar.            | The system displays a list of products matching the search criteria.                            |               |           |
| **Product Search - TC-02**        | Verify that the system shows an error message for invalid product searches.| An error message is displayed indicating that no products were found.                           |               |           |

### Shopping Cart Tests

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Shopping Cart - TC-01**         | Verify that users can add and remove items from the shopping cart.         | The item is removed from the cart, and the cart total is updated.                               |               |           |
| **Shopping Cart - TC-02**         | Verify that the shopping cart displays the correct total price after adding items.| The total price matches the sum of the prices of the items in the cart.                         |               |           |

### Checkout Tests

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Checkout - TC-01**              | Verify that the user can complete the checkout process.                    | The order is successfully placed, and the user receives a confirmation message.                 |               |           |

### Payment Tests

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Payment - TC-01**               | Verify that payments can be processed successfully.                        | Payment is processed, and the user receives a payment confirmation.                             |               |           |
| **Payment - TC-02**               | Verify that payment processing fails with invalid credit card details.     | An error message is displayed indicating payment failure.                                       |               |           |

### Backend Verification for Payment

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Backend Verification - TC-01**  | Verify that payment information is correctly stored in the database after a successful transaction.| The payment record exists in the database with the correct amount and user details.              |               |           |
| **Backend Verification - TC-02**  | Verify that failed payment attempts are logged in the database.            | A record of the failed payment attempt exists with the relevant error details.                   |               |           |
| **Backend Verification - TC-03**  | Verify that the order history reflects the correct payment status in the database.| The order history shows the correct status (completed, failed) based on payment outcome.         |               |           |

### User Functions Tests

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **User Functions - TC-01**        | Verify that users can reset their passwords successfully.                  | A confirmation message is sent to the user's email for password reset.                          |               |           |

### User Interface Tests

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **User Interface - TC-01**        | Verify that all links on the homepage are functional.                      | Each link navigates to the corresponding page without errors.                                   |               |           |

### Accessibility Tests

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Accessibility - TC-01**         | Verify that the website is navigable using keyboard-only controls.         | All links and buttons can be accessed and selected without a mouse.                             |               |           |
| **Accessibility - TC-02**         | Verify that all images have descriptive alt text for screen readers.       | Screen reader announces images correctly with their descriptions.                               |               |           |
| **Accessibility - TC-03**         | Verify that color contrast meets accessibility standards.                  | All text elements meet or exceed the required contrast ratio for readability.                   |               |           |

