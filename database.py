import sqlite3

# Initialize database and create tables
def init_db():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    # Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT CHECK(role IN ('admin', 'customer'))
    )''')

    # Cars table
    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        make TEXT,
        model TEXT,
        year INTEGER,
        mileage INTEGER,
        available INTEGER,
        min_rent_days INTEGER,
        max_rent_days INTEGER
    )''')

    # Rentals table
    cursor.execute('''CREATE TABLE IF NOT EXISTS rentals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        car_id INTEGER,
        start_date TEXT,
        end_date TEXT,
        status TEXT CHECK(status IN ('pending', 'approved', 'rejected')),
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(car_id) REFERENCES cars(id)
    )''')

    conn.commit()
    conn.close()