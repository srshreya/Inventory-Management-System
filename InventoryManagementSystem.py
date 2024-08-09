import mysql.connector
from getpass import getpass

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="password",  # Replace with your MySQL password
    database="InventoryManagement"
)

cursor = conn.cursor()

# Function to register a new user
def register_user(username, password, role):
    cursor.execute("""
        INSERT INTO Users (Username, Password, Role)
        VALUES (%s, %s, %s)
    """, (username, password, role))
    conn.commit()

# Function to authenticate a user
def login_user(username, password):
    cursor.execute("""
        SELECT Role FROM Users WHERE Username = %s AND Password = %s
    """, (username, password))
    result = cursor.fetchone()
    return result[0] if result else None

# Function to view products
def view_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    for product in products:
        print(product)

# Function to search for a product by name
def search_product(product_name):
    cursor.execute("SELECT * FROM Products WHERE ProductName LIKE %s", ('%' + product_name + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

# Admin-only functions
def add_product(product_name, quantity, price):
    cursor.execute("""
        INSERT INTO Products (ProductName, Quantity, Price)
        VALUES (%s, %s, %s)
    """, (product_name, quantity, price))
    conn.commit()

def update_product(product_id, product_name=None, quantity=None, price=None):
    if product_name:
        cursor.execute("UPDATE Products SET ProductName = %s WHERE ProductID = %s", (product_name, product_id))
    if quantity:
        cursor.execute("UPDATE Products SET Quantity = %s WHERE ProductID = %s", (quantity, product_id))
    if price:
        cursor.execute("UPDATE Products SET Price = %s WHERE ProductID = %s", (price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute("DELETE FROM Products WHERE ProductID = %s", (product_id,))
    conn.commit()

# Example usage
def main():
    while True:
        print("\nWelcome to Inventory Management System")
        print("1. Register")
        print("2. Login")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            role = input("Enter role (admin/user): ")
            register_user(username, password, role)
            print("Registration successful!")
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            role = login_user(username, password)

            if role:
                print(f"Login successful! Logged in as {role}")
                if role == 'admin':
                    while True:
                        print("\nAdmin Menu")
                        print("1. View Products")
                        print("2. Add Product")
                        print("3. Update Product")
                        print("4. Delete Product")
                        print("5. Search Product")
                        print("6. Logout")
                        admin_choice = input("Select an option: ")

                        if admin_choice == '1':
                            view_products()
                        elif admin_choice == '2':
                            product_name = input("Enter product name: ")
                            quantity = int(input("Enter quantity: "))
                            price = float(input("Enter price: "))
                            add_product(product_name, quantity, price)
                            print("Product added successfully!")
                        elif admin_choice == '3':
                            product_id = int(input("Enter product ID to update: "))
                            product_name = input("Enter new product name (leave blank to skip): ")
                            quantity = input("Enter new quantity (leave blank to skip): ")
                            price = input("Enter new price (leave blank to skip): ")
                            update_product(product_id, product_name or None, int(quantity) if quantity else None, float(price) if price else None)
                            print("Product updated successfully!")
                        elif admin_choice == '4':
                            product_id = int(input("Enter product ID to delete: "))
                            delete_product(product_id)
                            print("Product deleted successfully!")
                        elif admin_choice == '5':
                            product_name = input("Enter product name to search: ")
                            search_product(product_name)
                        elif admin_choice == '6':
                            break
                elif role == 'user':
                    while True:
                        print("\nUser Menu")
                        print("1. View Products")
                        print("2. Search Product")
                        print("3. Logout")
                        user_choice = input("Select an option: ")

                        if user_choice == '1':
                            view_products()
                        elif user_choice == '2':
                            product_name = input("Enter product name to search: ")
                            search_product(product_name)
                        elif user_choice == '3':
                            break
            else:
                print("Login failed! Invalid username or password.")

if _name_ == "_main_":
    main()

# Close the connection
cursor.close()
conn.close()
