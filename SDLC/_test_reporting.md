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

| Test Suite               | Total Tests | Pass/Fail                     |
|--------------------------|-------------|-------------------------------|
| User Registration        | 2           | 1 Pass, 1 Fail (invalid DOB)  |
| Product Search           | 2           | Pass                          |
| Shopping Cart            | 2           | 1 Pass, 1 Fail (retains old items) |
| Checkout Process         | 1           | Pass                          |
| Payment Gateway          | 2           | Pass                          |
| Backend Data Verification| 3           | Pass                          |
| User Functions           | 4           | 2 Pass, 2 Fail (order history, favourites issue) |
| User Interface           | 1           | Pass                          |
| Accessibility            | 3           | 2 Pass, 1 Fail (contrast)     |
| Boundary Testing         | 3           | Pass                          |
| State Transition Testing | 3           | Pass                          |
| Browser Testing          | 5           | Pass                          |

## 3. Bugs Identified

| Bug ID    | Area Affected       | Description                                                                 | Severity | Status     |
|-----------|---------------------|-----------------------------------------------------------------------------|----------|------------|
| BUG-001   | User Login          | Users unable to log in with valid credentials intermittently.               | High     | Open       |
| BUG-002   | User Registration   | User can sign up with an invalid Date of Birth (e.g., more than 200 years old).| Medium   | Open       |
| BUG-003   | Order History       | No ability to view previous orders on the order history page.               | High     | Open       |
| BUG-004   | Shopping Cart       | Shopping cart retains previously purchased items after checkout.            | Medium   | Open       |
| BUG-005   | Favorites Feature   | Fruit items are incorrectly added to the vegetable category on the favorites page.| Medium   | Open       |

## 4. Detailed Test Results

### 4.1 User Registration

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-UR-01              | Verify that a user can successfully register with valid info.       | User receives confirmation and is redirected to login page.  | As expected.                         | Pass      |
| TC-UR-02              | Verify that registration fails with invalid Date of Birth.          | Error message displayed for invalid DOB.                    | User successfully registers.         | Fail      |

### 4.2 Product Search

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-PS-01              | Verify that users can search for products using the search bar.     | Products matching the search criteria are displayed.         | As expected.                         | Pass      |
| TC-PS-02              | Verify that the system shows an error for invalid product searches. | Error message is displayed when no products are found.       | As expected.                         | Pass      |

### 4.3 Shopping Cart

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-SC-01              | Verify that users can add and remove items from the cart.           | Item is removed, and total is updated.                      | Retains old items after checkout.    | Fail      |
| TC-SC-02              | Verify that the shopping cart displays the correct total price.     | Total price matches the sum of items in the cart.            | As expected.                         | Pass      |

### 4.4 Checkout Process

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-CO-01              | Verify that the user can complete the checkout process.             | Order is placed, and a confirmation message is shown.        | As expected.                         | Pass      |

### 4.5 Payment Gateway

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-PG-01              | Verify that payments are processed successfully.                    | Payment processed, confirmation received.                   | As expected.                         | Pass      |
| TC-PG-02              | Verify that payment fails with invalid credit card details.         | Error message displayed for invalid card details.            | As expected.                         | Pass      |

### 4.6 Backend Data Verification

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-BV-01              | Verify payment information is stored in the database.               | Payment record exists with correct details.                 | As expected.                         | Pass      |
| TC-BV-02              | Verify that failed payment attempts are logged in the database.     | Failed payment record exists with error details.             | As expected.                         | Pass      |
| TC-BV-03              | Verify that order history reflects the correct payment status.      | Order history shows correct payment status.                 | As expected.                         | Pass      |

### 4.7 Accessibility

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-AC-01              | Verify that the site is navigable using keyboard-only controls.     | All links and buttons can be accessed without a mouse.       | As expected.                         | Pass      |
| TC-AC-02              | Verify that all images have descriptive alt text for screen readers.| Screen reader reads images correctly.                       | As expected.                         | Pass      |
| TC-AC-03              | Verify that color contrast meets accessibility standards.           | All text meets required contrast ratio for readability.      | Minor contrast issues found.         | Fail      |

### 4.8 Browser Testing

| Test ID               | Objective                                                           | Expected Result                                             | Actual Result                        | Pass/Fail |
|-----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|-----------|
| TC-BT-01              | Verify website functionality on Chrome.                            | All features work correctly and are visually accurate.       | As expected.                         | Pass      |
| TC-BT-02              | Verify website functionality on Firefox.                           | All features work correctly and are visually accurate.       | As expected.                         | Pass      |
| TC-BT-03              | Verify website functionality on Safari.                            | All features work correctly and are visually accurate.       | As expected.                         | Pass      |
| TC-BT-04              | Verify website functionality on Edge.                              | All features work correctly and are visually accurate.       | As expected.                         | Pass      |
| TC-BT-05              | Verify website responsiveness on mobile devices.                   | Fully functional and visually accurate on various devices.   | As expected.                         | Pass      |
