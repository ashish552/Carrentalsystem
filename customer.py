import sqlite3

class CustomerManager:
    def __init__(self, db_name='car_rental.db'):
        self.db_name = db_name

    def view_available_cars(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.execute("SELECT * FROM cars WHERE available = 1")
            cars = cur.fetchall()
            if not cars:
                print("No cars available.")
            for car in cars:
                (car_id, make, model, year, mileage, available, min_days, max_days) = car
                print(f"ID: {car_id}")
                print(f"Make: {make}")
                print(f"Model: {model}")
                print(f"Year: {year}")
                print(f"Mileage: {mileage}")
                print(f"Available: {'Yes' if available == 1 else 'No'}")
                print(f"Min Rent Days: {min_days}")
                print(f"Max Rent Days: {max_days}")
                print("-" * 40)

    def book_car(self, user_id):
        self.view_available_cars()
        try:
            car_id = int(input("Car ID to book: "))
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
        except ValueError:
            print("Invalid input.")
            return

        with sqlite3.connect(self.db_name) as conn:
            conn.execute(
                "INSERT INTO rentals (user_id, car_id, start_date, end_date, status) VALUES (?, ?, ?, ?, 'pending')",
                (user_id, car_id, start_date, end_date)
            )
            print("Booking requested.")
