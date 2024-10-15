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

## 4. Test Execution Details

- **Test Executed by**: QA Team
- **Test Execution Period**: Oct 10, 2024 - Oct 14, 2024
- **Test Environment**: 
  - OS: Windows 11
  - Browser: Google Chrome Version 116.0
  - Backend: Flask + SQLite (Test DB)
  - Frontend: React.js (v18)  
  - API: Stripe (for payment gateway)

## 5. Defects Summary

- **Shopping Cart - TC-01**: Removal of items from the cart does not work correctly; item remains in cart.
- **Accessibility - TC-03**: Contrast ratio issues with certain text elements affecting readability for visually impaired users.

## 6. Recommendations

- **Shopping Cart Issue**: Investigate the logic for item removal from the cart and ensure that the cart is updated both on the frontend and backend.
- **Accessibility Issue**: Improve color contrast for better readability in line with accessibility guidelines (WCAG 2.1).

---
Prepared by: **Edina**  
Date: Oct 14, 2024

