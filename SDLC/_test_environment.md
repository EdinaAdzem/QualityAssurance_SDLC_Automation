# Environment Setup for Grocery Mate Webshop

This document outlines the environment, tools, and infrastructure required to develop, test, and run the Grocery Mate Webshop project.

## Project URL
- [Grocery Mate Webshop](https://grocerymate.masterschool.com/)

---

## 1. Software Requirements

### For Development:
- **Operating System**: Windows, macOS, or Linux
- **Backend**:
  - **Language**: Python 3.10+ or Node.js 16+
  - **Framework**: Flask (Python) or Express (Node.js)
  - **Database**: SQLite (for lightweight local development) or MySQL (for production-like setup)
  - **Environment Management**: `dotenv` for secure environment variable management
- **Frontend**:
  - **Languages**: HTML5, CSS3, JavaScript (ES6+)
  - **Frameworks**: React.js (preferred) or vanilla JavaScript
  - **CSS Preprocessor**: SASS (recommended) or plain CSS
  - **Package Manager**: npm for dependency management

### For Testing:
- **Browsers**: Google Chrome, Firefox (for cross-browser compatibility tests)
- **Testing Tools**:
  - **Unit Testing**: Pytest (Python) or Jest (JavaScript)
  - **End-to-End Testing**: Cypress
- **Mocking APIs**: Postman or Mockoon (for API testing)

### **For Deployment**:  
- **Web Servers**: Nginx (reverse proxy) or Apache  
- **Cloud Services**: AWS or Azure (if applicable)  

---

## 2. Infrastructure and Environment Setup

### **Architecture**:
- **Frontend**: React-based single-page application (served via Nginx or Apache)
- **Backend**: RESTful API implemented using Flask or Express.js
- **Database**: MySQL database hosted on AWS RDS or a similar service

### **Servers**:
- **Web Server**:  
  - IP: `192.168.x.x` (local development) or a public IP for staging/production  
  - Role: Serves static content and routes API requests  
- **Database Server**:  
  - IP: `192.168.x.y`  
  - Role: Handles relational database queries for product data, user authentication, and transactions  

### **Security**:
- **Authentication**: JWT-based user authentication for secure sessions  
- **Authorization**: Role-based access control for admin vs user actions  

### **Deployment**:
- **CI/CD Pipeline**:
  - **Tools**: GitHub Actions, Jenkins, or CircleCI  
  - **Workflow**:
    1. Push code to GitHub  
    2. Run automated tests (unit and integration)  
    3. Build Docker containers  
    4. Deploy containers to AWS ECS or Azure App Service  

---

## 3. Dependencies

### Backend Dependencies:
- Flask (for Python) or Express (for Node.js)
- SQLAlchemy (if using Python)
- Mongoose (if using MongoDB with Node.js)
- dotenv for environment variable management

### Frontend Dependencies:
- React or any other JavaScript framework (if applicable)
- swagger (for API calls)

---

## 4. Tools

- **Version Control**: Git  
- **Code Editor**: Pycharm primerily, but: VSCode, Sublime Text, or any preferred IDE  
- **Testing Framework**:  
  - Unit Tests: Pytest (Python) or Jest (JavaScript)  
  - End-to-End Tests: Tool can be decided by the team
- **APIs**:  
  - Mocking Tools: Postman or swagger API simulation  

---
