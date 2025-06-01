import sqlite3

class AdminManager:
    def __init__(self, db_name='car_rental.db'):
        self.db_name = db_name #Name of the SQLite database File

    def add_car(self):
        #Get car details from the admin 
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        mileage = int(input("Mileage: "))
        available = int(input("Available (1=Yes, 0=No): "))
        min_days = int(input("Min rental days: "))
        max_days = int(input("Max rental days: "))
        daily_rate = float(input("Enter daily rental rate: "))
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                "INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, daily_rate) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (make, model, year, mileage, available, min_days, max_days, daily_rate)
            )
            print("Car added.")

    def update_car(self):
        # Repeatedly ask for a valid car ID until found
        while True:
            car_id_input = input("Car ID: ")
            try:
                car_id = int(car_id_input)
            except ValueError:
                print("Invalid input. Please enter a valid integer ID. ")
                continue

            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.execute("SELECT id FROM cars WHERE id = ?", (car_id,))
                result = cursor.fetchone()
                if result:
                    break
                else:
                    print("Car ID not found. Please enter a valid ID.")

        
        allowed_fields = {
            "make", 'model', 'year', 'mileage', 'available', 'min_rent_days', 'max_rent_days'
        }
        print("Allowed fields to update: make, model, year, mileage, available, min_rent_days, max_rent_days")
        field = input("Field to update: ").strip().lower()

        if field not in allowed_fields:
            print(f" Error: '{field}' is not a valid field.")
            return
        
        value = input("New value: ")

        if field in {"year", "mileage", "min_rent_days", "max_rent_days"}:
              try:
                  value = int(value)
              except ValueError:
                print(" Error: This field requires a numeric value.")
                return
              
        if field == "available" and value.lower() not in {"yes", "no"}:
            print(" Error: 'available' must be 'yes' or 'no'.")
            return
   

        with sqlite3.connect(self.db_name) as conn:
            conn.execute(f"UPDATE cars SET {field} = ? WHERE id = ?", (value, car_id))
            print("Car updated.")


    # Delete the car from the database
    def delete_car(self):
        while True:
            car_id_input = input("Car ID: ")
            try:
                car_id = int(car_id_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer ID. ")

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("DELETE FROM cars WHERE id = ?", (car_id,))
            if cursor.rowcount > 0:
                print("Car deleted. ")
            else:
                print("Car ID not found.")

    def manage_bookings(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("""
                SELECT rentals.id, users.username, cars.make, cars.model, 
                       rentals.start_date, rentals.end_date, rentals.status
                FROM rentals
                JOIN users ON rentals.user_id = users.id
                JOIN cars ON rentals.car_id = cars.id
            """)
            bookings = cursor.fetchall()
            for booking in bookings:
                 booking_id, customer, make, model, start_date, end_date, status = booking
                 print(f"""
                    Booking ID   = {booking_id}
                    Customer     = {customer}
                    Make         = {make}
                    Model        = {model}
                    Start Date   = {start_date}
                    End Date     = {end_date}
                    Status       = {status}
                        """)
           
            user_input = input("Rental ID to manage: ")
            try:
                rental_id = int(user_input)
                cursor = conn.execute("SELECT id FROM rentals WHERE id = ? AND status = 'pending'", (rental_id,))
                if cursor.fetchone() is None:
                    print("Rental ID cannot found or already processed. Please enter a valid pending Rental ID.")
                    return
            
            except ValueError:
                print('Invalid ID. Please enter a number..')
                return

            while True:
                 decision = input("Approve or reject: ").lower()
                 if decision == 'approve':
                    status = 'approved'
                    break
                 elif decision == "reject":
                    status = 'rejected'
                    break
                 else: 
                     print("Invalid decision. Please type 'approve' or 'reject'. ")


            # Update rental status
            conn.execute("UPDATE rentals SET status = ? WHERE id  = ?", (status, rental_id))
            print(f"Rental ID {rental_id} has been {status}.")
