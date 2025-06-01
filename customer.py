import sqlite3
from datetime import datetime

class CustomerManager:
    def __init__(self, db_name='car_rental.db'):
        self.db_name = db_name

     # Display all available cars (available = 1)
    def view_available_cars(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.execute("SELECT * FROM cars WHERE available = 1")
            cars = cur.fetchall()
            if not cars:
                print("No cars available.")
            for car in cars:
                (car_id, make, model, year, mileage, available, min_days, max_days, daily_rate) = car
                print(f"ID: {car_id}")
                print(f"Make: {make}")
                print(f"Model: {model}")
                print(f"Year: {year}")
                print(f"Mileage: {mileage}")
                print(f"Available: {'Yes' if available == 1 else 'No'}")
                print(f"Min Rent Days: {min_days}")
                print(f"Max Rent Days: {max_days}")
                print(f"Daily Rate: ${daily_rate}")
                print("-" * 40)

    #Book the car with ID
    def book_car(self, user_id):
        self.view_available_cars()
        try:
            car_id = int(input("Car ID to book: "))
            start_input = input("Start date (YYYY-MM-DD): ")
            end_input = input("End date (YYYY-MM-DD): ")

            start_date = datetime.strptime(start_input, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_input, "%Y-%m-%d").date()

            if start_date >= end_date:
                print("End date must be after start date. ")
        except ValueError:
            print("Invalid input.")
            return
        
        rental_days = (end_date - start_date).days

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("SELECT daily_rate, min_rent_days, max_rent_days FROM cars WHERE id = ? AND available = 1", (car_id,))
            result = cursor.fetchone()
            if not result:
                print("car not found or not available.")
                return
            
            daily_rate, min_days, max_days = result

            if daily_rate is None:
                print("Error: Daily rate for this car is not set. ")
                return
            
            if rental_days < min_days or rental_days > max_days:
                print(f"Rental duration must be between {min_days} and {max_days} days. ")
                return
            
            additional_charge = 0
            rental_fee = rental_days * daily_rate + additional_charge

            print(f"Rental duration: {rental_days} day(s)")
            print(f"Daily Rate: ${daily_rate:.2f}")
            print(f"Additional Charges: ${additional_charge:.2f}")
            print(f"Total Rental Fee: ${rental_fee:.2f}")

            #Confirm Booking
            confirm = input("Do you want to proceed with th booking? (yes/no): ").lower()
            if confirm != 'yes':
                print("Booking cancelled.")
                return
            
            conn.execute(
                "INSERT INTO rentals (user_id, car_id, start_date, end_date, status, rental_fee) VALUES (?, ?, ?, ?, 'pending', ?)",
                (user_id, car_id, str(start_date), str(end_date), rental_fee)
            )
            print("Booking requested.")
