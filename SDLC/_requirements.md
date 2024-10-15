# Requirements for Grocery Mate Webshop

## 1. User Registration

- **R1.1**: The system must allow users to register with valid information.
- **R1.2**: The system must not allow registration with an already existing username.
- **R1.3**: Upon successful registration, the system must provide a confirmation message and redirect the user to the login page.
- **R1.4**: If the username already exists, an error message must be displayed to the user.

## 2. Product Search

- **R2.1**: The system must allow users to search for products using a search bar.
- **R2.2**: The system must display a list of products that match the search criteria.
- **R2.3**: If no products match the search criteria, the system must display an error message stating that no products were found.

## 3. Shopping Cart

- **R3.1**: The system must allow users to add and remove items from the shopping cart.
- **R3.2**: The shopping cart must display the total price of the items added.
- **R3.3**: The total price in the shopping cart must be updated whenever an item is added or removed.
- **R3.4**: The total price displayed must correctly reflect the sum of the prices of the items in the cart.

## 4. Checkout

- **R4.1**: The system must allow users to complete the checkout process.
- **R4.2**: Upon successful order placement, the system must display a confirmation message to the user.

## 5. Payment

- **R5.1**: The system must process valid payment information successfully.
- **R5.2**: The system must display a payment confirmation message after successful payment.
- **R5.3**: The system must reject invalid payment information and display an error message indicating payment failure.

## 6. Backend Verification for Payment

- **R6.1**: The system must store payment information in the database after successful payment.
- **R6.2**: The system must log failed payment attempts in the database, including relevant error details.
- **R6.3**: The order history in the database must reflect the correct payment status (completed or failed) based on the payment outcome.

## 7. User Functions

- **R7.1**: The system must allow users to reset their passwords.
- **R7.2**: The system must send a password reset confirmation to the user's email.

## 8. User Interface

- **R8.1**: All links on the homepage must be functional.
- **R8.2**: Clicking a link on the homepage must navigate to the corresponding page without any errors.

## 9. Accessibility

- **R9.1**: The system must be fully navigable using keyboard-only controls.
- **R9.2**: All images on the website must have descriptive alt text for screen readers.
- **R9.3**: The website must meet or exceed the required color contrast ratio for readability and accessibility compliance.
