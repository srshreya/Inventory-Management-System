# Inventory Management System

This is a Python-based Inventory Management System using MySQL for database management. The system allows for user registration, login, and product management with different access levels for admins and regular users.

## Features

- **User Registration:** Register new users with specific roles (admin or user).
- **User Authentication:** Login functionality with role-based access control.
- **Admin Functions:**
  - View all products.
  - Add new products.
  - Update existing products.
  - Delete products.
  - Search for products by name.
- **User Functions:**
  - View all products.
  - Search for products by name.

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   cd inventory-management-system
2. Install the required Python packages:
   pip install mysql-connector-python
   
3. Set up the MySQL database:
   - Create a MySQL database named InventoryManagement.
   - Create the required tables using the following SQL schema.
     
4. Update the database connection details in the main.py file.
