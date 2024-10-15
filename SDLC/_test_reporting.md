# Test Reporting for Grocery Mate Webshop

This document summarizes the testing process and the results of various test cases executed for the Grocery Mate Webshop project.

## 1. Overview

The purpose of this test report is to evaluate the quality and stability of the Grocery Mate Webshop before deployment. The following key areas were tested:
- User Registration
- Product Search
- Shopping Cart
- Checkout Process
- Payment Gateway
- Backend Data Verification
- User Functions
- User Interface
- Accessibility Compliance

## 2. Test Summary

| Test Suite            | Total Tests | Comments                       |
|-----------------------|-------------|--------------------------------|
| User Registration      | 2           | Registration works as expected. |
| Product Search         | 2           | Search functionality verified.  |
| Shopping Cart          | 2           | Issue with item removal found.  |
| Checkout Process       | 1           | Checkout successful.            |
| Payment Gateway        | 2           | Payment processed successfully. |
| Backend Verification   | 3           | Data integrity verified.         |
| User Functions         | 1           | Password reset verified.         |
| User Interface         | 1           | All links are functional.        |
| Accessibility          | 3           | Color contrast issue found.     |

## 3. Detailed Test Results

### 3.1 User Registration

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| User Registration - TC-01 | Verify that a user can successfully register with valid info.       | User receives confirmation and is redirected to login page.  | As expected.                         |
| User Registration - TC-02 | Verify that registration fails with an already existing username.  | Error message displayed for duplicate username.              | Error displayed correctly.           |

### 3.2 Product Search

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| Product Search - TC-01  | Verify that users can search for products using the search bar.     | Products matching the search criteria are displayed.         | Search results displayed correctly.  |
| Product Search - TC-02  | Verify that the system shows an error for invalid product searches. | Error message is displayed when no products are found.       | Error message displayed as expected. |

### 3.3 Shopping Cart

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| Shopping Cart - TC-01  | Verify that users can add and remove items from the cart.            | Item is removed and total is updated.                       | Issue with item removal.             |
| Shopping Cart - TC-02  | Verify that the shopping cart displays the correct total price.      | Total price matches the sum of items in the cart.            | Price calculation is correct.        |

### 3.4 Checkout Process

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| Checkout - TC-01       | Verify that the user can complete the checkout process.             | Order is placed, and a confirmation message is shown.        | Order placed successfully.           |

### 3.5 Payment Gateway

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| Payment - TC-01        | Verify that payments are processed successfully.                    | Payment processed, confirmation received.                   | Payment processed as expected.       |
| Payment - TC-02        | Verify that payment fails with invalid credit card details.         | Error message displayed for invalid card details.            | Error message displayed as expected. |

### 3.6 Backend Data Verification

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| Backend - TC-01        | Verify payment information is stored in the database.               | Payment record exists with correct details.                 | Record found in database.            |
| Backend - TC-02        | Verify that failed payment attempts are logged in the database.     | Failed payment record exists with error details.             | Failure logged correctly.            |
| Backend - TC-03        | Verify that order history reflects the correct payment status.      | Order history shows correct payment status.                 | Status updated as expected.          |

### 3.7 User Functions

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| User Functions - TC-01 | Verify that users can reset their passwords successfully.           | Confirmation message sent to email for password reset.       | Message sent and password reset.     |

### 3.8 User Interface

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| UI - TC-01             | Verify that all links on the homepage are functional.               | Each link navigates to the corresponding page.               | Links work as expected.              |

### 3.9 Accessibility

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| Accessibility - TC-01  | Verify that the site is navigable using keyboard-only controls.     | All links and buttons can be accessed without a mouse.       | Keyboard navigation works fine.      |
| Accessibility - TC-02  | Verify that all images have descriptive alt text for screen readers.| Screen reader reads images correctly.                       | Alt text provided correctly.         |
| Accessibility - TC-03  | Verify that color contrast meets accessibility standards.           | All text meets required contrast ratio for readability.      | Minor contrast issues found.         |

## 4. Boundary and State Transition Testing

### 4.1 Boundary Testing

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| Boundary - TC-01      | Verify that the user cannot register with a username shorter than 3 characters. | Error message displayed for username too short.            | As expected.                         |
| Boundary - TC-02      | Verify that the user cannot register with a username longer than 20 characters. | Error message displayed for username too long.             | As expected.                         |
| Boundary - TC-03      | Verify that the shopping cart accepts a maximum of 50 items.       | Error message displayed when trying to add more than 50 items. | As expected.                         |

### 4.2 State Transition Testing

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|
| State Transition - TC-01 | Verify that the user can transition from "Logged Out" to "Logged In" after successful login. | User is redirected to the dashboard.                        | As expected.                         |
| State Transition - TC-02 | Verify that the user can transition from "Shopping Cart" to "Checkout" after clicking the checkout button. | User is redirected to the payment page.                    | As expected.                         |
| State Transition - TC-03 | Verify that the order status changes from "Pending" to "Completed" after payment is successful. | Order status updated correctly in order history.           | As expected.                         |

## Browser Testing with BrowserStack

| Test ID                          | Objective                                                                 | Expected Result                                                                                 | Actual Result | Pass/Fail |
|-----------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|-----------|
| **Browser Testing - TC-01**       | Verify website functionality on Chrome.                                   | All features work correctly and are visually accurate on the Chrome browser.                    |               |           |
| **Browser Testing - TC-02**       | Verify website functionality on Firefox.                                  | All features work correctly and are visually accurate on the Firefox browser.                   |               |           |
| **Browser Testing - TC-03**       | Verify website functionality on Safari.                                   | All features work correctly and are visually accurate on the Safari browser.                    |               |           |
| **Browser Testing - TC-04**       | Verify website functionality on Edge.                                     | All features work correctly and are visually accurate on the Edge browser.                      |               |           |
| **Browser Testing - TC-05**       | Verify website responsiveness on mobile devices using BrowserStack.       | The website is fully functional and visually accurate on various mobile devices.                 |               |           |

## Test Case Summary

| Test ID                       | Objective                                                                 | Expected Result                                                                         | Actual Result | 
|-------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------|
| User Registration - TC-01     | Verify that a user can successfully register with valid information.     | User receives a confirmation message and is redirected to the login page.             |               |
| User Registration - TC-02     | Verify that registration fails with an already existing username.        | An error message is displayed indicating that the username already exists.            |               |
| Product Search - TC-01       | Verify that users can search for products using the search bar.         | The system displays a list of products matching the search criteria.                   |               |
| Product Search - TC-02       | Verify that the system shows an error message for invalid product searches.| An error message is displayed indicating that no products were found.                  |               |
| Shopping Cart - TC-01        | Verify that users can add and remove items from the cart.               | The item is removed, and the total is updated accordingly.                            |               |
| Shopping Cart - TC-02        | Verify that the shopping cart displays the correct total price.         | The total price displayed matches the sum of items in the cart.                        |               |
| Checkout - TC-01              | Verify that the user can complete the checkout process.                 | The order is placed, and a confirmation message is displayed.                          |               |
| Payment - TC-01               | Verify that payments are processed successfully.                        | Payment is processed successfully, and a confirmation message is displayed.            |               |
| Payment - TC-02               | Verify that payment fails with invalid credit card details.             | An error message is displayed indicating that the credit card details are invalid.     |               |
| Backend - TC-01               | Verify payment information is stored in the database.                   | A payment record exists in the database with the correct details.                       |               |
| Backend - TC-02               | Verify that failed payment attempts are logged in the database.         | A failed payment record exists in the database with the appropriate error details.      |               |
| Backend - TC-03               | Verify that order history reflects the correct payment status.          | The order history displays the correct payment status.                                   |               |
| User Functions - TC-01        | Verify that users can reset their passwords successfully.               | A confirmation message is sent to the user's email for the password reset.             |               |
| UI - TC-01                    | Verify that all links on the homepage are functional.                   | Each link navigates to the corresponding page as expected.                             |               |
| Accessibility - TC-01         | Verify that the site is navigable using keyboard-only controls.         | All links and buttons can be accessed without a mouse.                                 |               |
| Accessibility - TC-02         | Verify that all images have descriptive alt text for screen readers.    | The screen reader reads the images correctly with appropriate descriptions.              |               |
| Accessibility - TC-03         | Verify that color contrast meets accessibility standards.               | All text meets the required contrast ratio for readability.                             |               |
| Boundary - TC-01              | Verify that the user cannot register with a username shorter than 3 characters. | An error message is displayed indicating that the username is too short.                |               |
| Boundary - TC-02              | Verify that the user cannot register with a username longer than 20 characters. | An error message is displayed indicating that the username is too long.                 |               |
| Boundary - TC-03              | Verify that the shopping cart accepts a maximum of 50 items.          | An error message is displayed when attempting to add more than 50 items to the cart.   |               |
| State Transition - TC-01      | Verify that the user can transition from "Logged Out" to "Logged In" after successful login. | The user is redirected to the dashboard after logging in.                                |               |
| State Transition - TC-02      | Verify that the user can transition from "Shopping Cart" to "Checkout". | The user is redirected to the payment page after clicking the checkout button.           |               |
| State Transition - TC-03      | Verify that the order status changes from "Pending" to "Completed" after payment is successful. | The order status is updated correctly in the order history.                              |               |
| Browser Testing - TC-01       | Verify website functionality on Chrome.                                 | All features work correctly and are visually accurate on the Chrome browser.            |               |
| Browser Testing - TC-02       | Verify website functionality on Firefox.                                | All features work correctly and are visually accurate on the Firefox browser.           |               |
| Browser Testing - TC-03       | Verify website functionality on Safari.                                 | All features work correctly and are visually accurate on the Safari browser.            |               |
| Browser Testing - TC-04       | Verify website functionality on Edge.                                   | All features work correctly and are visually accurate on the Edge browser.              |               |
| Browser Testing - TC-05       | Verify website responsiveness on mobile devices using BrowserStack.     | The website is fully functional and visually accurate on various mobile devices.         |               |

## 5. Conclusion

Overall, the Grocery Mate Webshop has passed most of the critical test cases with a few issues noted for further investigation. The following actions are recommended:
- Resolve the shopping cart item removal issue.
- Address the accessibility color contrast issue.
- Perform regression testing after fixes are implemented.

