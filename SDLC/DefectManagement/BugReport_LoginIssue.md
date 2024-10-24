# Bug Report: User can sign up with an invalid Date of Birth (more than 200 years old)

**Priority:** Medium  
**Reporter:** Edina 
**Date:** 19-08-2024  

**Environment:** Test  
**Application:** GroceryMate  
**Page:** Sign up Page  
**Browser:** Chrome  
**Operating System:** Windows  

## Steps to Reproduce:

1. Go to the GroceryMate login page.
2. Click on "Sign up" to be directed to the sign-up page.
3. Fill in 'InputValidationTest' as the username.
4. Enter '19-08-1820' as the Date of Birth.
5. Write 'This is my Bio' in the bio field.
6. Enter 'edina@faculty.masterschool.com' as the email address.
7. Set the password to 'somePass123'.
8. Click on the "Sign up" button.

## Expected Result:
An error message should appear indicating that the Date of Birth is invalid (user cannot be 200 years old).

## Actual Result:
No error message is displayed, and the user is still able to sign up.

## Screenshots/Attachments: