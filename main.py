# Import required classes and functions from other modules
from database import init_db
from user import UserManager
from admin import AdminManager
from customer import CustomerManager

# Menu shown to all users initially
def menu():
    print(" \n---- user manager -------")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

# Main function that controls the program flow
def main():
    user_manager = UserManager()
    customer_manager = CustomerManager()
    admin_manager = AdminManager()
    init_db()

    # Infinite loop for the main menu
    while True:
        menu()
        choice = input("Select an option(1-3): ")
        if choice == "1":
            user_manager.register()
        elif choice == "2":
            user = user_manager.login()
            # If login is successful, proceed based on user role
            if user:
                user_id, _, role = user
                if role == "admin":
                   while True:
                    admin_action = input(" \n1. Add car\n2. Update car\n3. Delete car\n4. Manage Bookings\n5. Logout\nselect an option from (1-5): ")
                    if admin_action == "1":
                        admin_manager.add_car()
                    elif admin_action == "2":
                        admin_manager.update_car()
                    elif admin_action == "3":
                        admin_manager.delete_car()
                    elif admin_action == "4":
                        admin_manager.manage_bookings()
                    elif admin_action == "5":
                        break
                elif role == "customer":
                    while True:
                        cust_action = input("\n1. View cars details\n2. Book car\n3. Logout \nSelect an option from (1-3): ")
                        if cust_action == '1':
                            customer_manager.view_available_cars()
                        elif cust_action == '2':
                            customer_manager.book_car(user_id)
                        elif cust_action == '3': # Log out customer
                            break
        elif choice == "3":
            break # Exit the application

if __name__ == "__main__":
    main()
