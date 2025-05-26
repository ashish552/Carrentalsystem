from database import init_db
from user import UserManager

def menu():

    print("\n ---- user manager -------")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def main():
    user_manager = UserManager()
    init_db()

    while True:
        menu()
        choice = input("Select an option(1-3): ")
        if choice == "1":
            user_manager.register()
        elif choice == "2":
            user = user_manager.login()
            if user:
                user_id, _, role = user
                print(f"✅ Logged in as {role.capitalize()} (User ID: {user_id})")
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
