import sqlite3

class UserManager:
    def __init__(self, db_name='car_rental.db'):
        self.db_name = db_name # Name of the SQLite database file

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/customer): ").lower()
        # Insert the new user into the 'users' table

        with sqlite3.connect(self.db_name) as conn:
            try:
                conn.execute(
                    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                    (username, password, role)
                )
                print("Registration successful.")
            except sqlite3.IntegrityError:
                print("Username already exists.")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute(
                "SELECT id, username, role FROM users WHERE username=? AND password=?",
                (username, password)
            )
            user = cursor.fetchone()

            if user:
                 # If found, login is successful
                print(f"Login successful as {user[2]}")
                return user  
            else:
                # If no matching user, login failed
                print("Invalid credentials.")
                return None
