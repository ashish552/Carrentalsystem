Car Rental System(CLI based):
A Car Rental System developed with Python and SQLite3 which allows Admins and Customers different access roles. The system has the ability for users to register, login, handle cars (data entry, modification and deletion), book a rental and finally approve any booked rentals.

Fetaures:
1. User Management: Register/ Login as admin or customer

2. Admin Function: Admin can add, update and delete car records and can manage (Approve/Reject) rental request from the customer.

3. Customer Function: Customer can view available car details and can book car with rental duration and fee calculation.

Installation and setup:
1. Clone the Repository
git clone https://github.com/ashish552/Carrentalsystem.git

2. Run the main program
python main.py

Upon the first time running the system, SQLite will have it database created and add all necessary tables automatically.

Project Structure

| File            | Purpose                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| `main.py`       | The initial area users go through when using the application. Manages the way Admins and Customers navigate the system. |
| `database.py`   | Creates and manages the SQLite database structure.                                                                      |
| `user.py`       | Handles user registration and login.                                                                                    |
| `admin.py`      | Allows Admins to manage cars and confirm/reject requests for booking.                                                   |
| `customer.py`   | Allows Customers to view and book available cars.                                                                       |
| `car_rental.db` | SQLite3 database created at runtime to store users, cars, and rental bookings.                                          |


Usage guide:
Register or Run:
1. Run main.py
2. Choose:
    a. [1] Register: It creates a new user(admin/customer).
    b. [2] Login: Login to system using you username and password.
    c. [3] Exit: Exiting out of the system

Admin Option(after Login):
a. [1] Add car: Input details of a car to add a new car
b. [2] Update car: Update the specific fields of a car which needs to be updated.
c. [3] Delete car: Removes the car from a database.
d. [4] Manage Bookings: View pending bookin request and approve/ reject them.
e. [5] Logout: Logout from admin

Customer option(after Login):
a. [1] View car details: Veiw all the cars that are available and their details.
b. [2] Book car: Select a car and  submit the dates you require to book a car.
c. [3] Logout: Logout from customer.

Known Issues/ Bugs
1. No password hashing: Passwords are kept without encryption. It needs to be secured at all times in production.
2. Because of its simplicity, input validation can sometimes accept invalid inputs.
3. No booking overlap checks: More than one customer may book the same car on the same dates.
4. No email/notification system for booking confirmation

Licensing:
MIT License Ashish
Copyright (c) 2025 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.





