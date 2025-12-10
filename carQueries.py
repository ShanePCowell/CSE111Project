import sqlite3
from sqlite3 import Error

import os
import project

def compareVehicles(_conn):
    ## COMPARE VEHICLES FUNCTION ##
    project.clear_screen()
    c=_conn.cursor()
    c.execute("SELECT c_model, c_make FROM car")
    row=c.fetchall()
    for i in range(len(row)):
        print(f"Vehicle '{i+1}': " +  row[i][1] + " " +  row[i][0])    
    value = False
    while not value:
        try:
            v1 = int(input("Select First Vehicle to Compare: "))
            v2 = int(input("Select Second Vehicle to Compare: "))
            value = True
        except ValueError:
            print(" Invalid input. Please try again.")

    project.clear_screen()
    print(f"Comparing '{row[v1-1][0]}' and '{row[v2-1][0]}':")

    c.execute("SELECT c_year FROM car")
    row1=c.fetchall()
    c.execute("SELECT c_wheelBase FROM car")
    row2=c.fetchall()
    c.execute("SELECT c_bodyType FROM car")
    row3=c.fetchall()

    print(f" - Year: {row1[v1-1][0]} vs {row1[v2-1][0]}")
    print(f" - Wheel Base: {row2[v1-1][0]} vs {row2[v2-1][0]}")
    print(f" - Body Type: {row3[v1-1][0]} vs {row3[v2-1][0]}")

    c.execute(f"SELECT t_id, count(t_id), max(t_accel), max(t_eco), max(t_weight), max(t_speed), min(t_price) FROM trim WHERE t_model = '{row[v1-1][0]}'")
    trims1=c.fetchall()
    c.execute(f"SELECT t_id, count(t_id), max(t_accel), max(t_eco), max(t_weight), max(t_speed), min(t_price) FROM trim WHERE t_model = '{row[v2-1][0]}'")
    trims2=c.fetchall()
    print(f" - Number of Trims: {trims1[0][1]} vs {trims2[0][1]}")
    print(f" - Best Acceleration: {trims1[0][2]} vs {trims2[0][2]}")
    print(f" - Best MPG: {trims1[0][3]} vs {trims2[0][3]}")
    print(f" - Heaviest Trim: {trims1[0][4]} vs {trims2[0][4]}")
    print(f" - Highest Top Speed: {trims1[0][5]} vs {trims2[0][5]}")
    print(f" - Lowest Price: ${trims1[0][6]} vs ${trims2[0][6]}")

    ##Get highest horsepower of each vehicle
    c.execute(f"SELECT max(e_horsepower) FROM engine JOIN trim on e_id=t_engine WHERE t_model = '{row[v1-1][0]}'")
    hp1=c.fetchall()
    c.execute(f"SELECT max(e_horsepower) FROM engine JOIN trim on e_id=t_engine WHERE t_model = '{row[v2-1][0]}'")
    hp2=c.fetchall()
    print(f" - Highest Horsepower: {hp1[0][0]} vs {hp2[0][0]}")

    c.execute(f"SELECT max(tr_gears) FROM transmission JOIN trim on tr_id=t_transmission WHERE t_model = '{row[v1-1][0]}'")
    gears1=c.fetchall()
    c.execute(f"SELECT max(tr_gears) FROM transmission JOIN trim on tr_id=t_transmission WHERE t_model = '{row[v2-1][0]}'")
    gears2=c.fetchall()
    print(f" - Highest Number of Gears: {gears1[0][0]} vs {gears2[0][0]}") 

    c.execute(f"SELECT max(w_diameter) FROM wheel JOIN trim on w_id=t_wheels WHERE t_model = '{row[v1-1][0]}'")
    wheel1=c.fetchall()
    c.execute(f"SELECT max(w_diameter) FROM wheel JOIN trim on w_id=t_wheels WHERE t_model = '{row[v2-1][0]}'")
    wheel2=c.fetchall()
    print(f" - Biggest Rims: {wheel1[0][0]} vs {wheel2[0][0]}")

    c.execute(f"SELECT COUNT(DISTINCT ct.c_id) FROM trim t JOIN color_Trim ct ON ct.t_id = t.t_model || '-' || t.t_id WHERE t.t_model = '{row[v1-1][0]}'")
    colors1=c.fetchall()
    c.execute(f"SELECT COUNT(DISTINCT ct.c_id) FROM trim t JOIN color_Trim ct ON ct.t_id = t.t_model || '-' || t.t_id WHERE t.t_model = '{row[v2-1][0]}'")
    colors2=c.fetchall()
    print(f" - Number of Colors Available: {colors1[0][0]} vs {colors2[0][0]}")

    print("\n")

    input("Press Enter to return to the main menu...")
    project.baseMenu(_conn)

def SeeStats(_conn):
    ## SEE STATS FUNCTION ##
    project.clear_screen()
    c=_conn.cursor()
    c.execute("SELECT c_model FROM car")
    row=c.fetchall()
    for i in range(len(row)):
        print(f"Vehicle '{i+1}': " +  row[i][0])    
    value = False
    while not value:
        try:
            v1 = int(input("Select Vehicle to see stats: "))
            value = True
        except ValueError:
            print(" Invalid input. Please try again.")
    project.clear_screen()        
    print(f"Stats for '{row[v1-1][0]}':")
    c.execute(f"SELECT * FROM car WHERE c_model = '{row[v1-1][0]}'")
    carStats=c.fetchall()
    print ("NAME: YEAR: MAKE: BODY TYPE: WHEEL BASE:")
    print(str(carStats[0]) + "\n")

    c.execute(f"SELECT t_id, t_engine, t_transmission, t_wheels, t_price, t_accel, t_eco, t_weight, t_speed FROM trim WHERE t_model = '{row[v1-1][0]}'")
    trimStats=c.fetchall()
    for i in range(len(trimStats)):
        print("Trim " + str(i+1))
        print("NAME: ENGINE: TRANSMISSION: WHEELS: PRICE: ACCELERATION: MPG: WEIGHT: TOP SPEED:")
        print(str(trimStats[i]) + "\n")

    c.execute(f"SELECT DISTINCT e_id, e_horsepower, e_torque, e_redline, e_fuelType, e_cylinders, e_displacement FROM engine JOIN trim on e_id=t_engine WHERE t_model = '{row[v1-1][0]}'")
    trimStats=c.fetchall()
    for i in range(len(trimStats)):
        print(trimStats[i][0])
        print("ID: HORSEPOWER: TORQUE: REDLINE: FUELTYPE: CYLINDERS: DISPLACEMENT:")
        print(str(trimStats[i]) + "\n")
    
    c.execute(f"SELECT DISTINCT tr_id, tr_type, tr_gears, tr_driveType, tr_driveRatio FROM transmission JOIN trim on tr_id=t_transmission WHERE t_model = '{row[v1-1][0]}'")
    trimStats=c.fetchall()
    for i in range(len(trimStats)):
        print(trimStats[i][0])
        print("ID: TYPE: GEARS: DRIVETYPE: DRIVERATIO:")
        print(str(trimStats[i]) + "\n")
    
    c.execute(f"SELECT DISTINCT w_id, w_diameter, w_rim, w_size FROM wheel JOIN trim on w_id=t_wheels WHERE t_model = '{row[v1-1][0]}'")
    trimStats=c.fetchall()
    for i in range(len(trimStats)):
        print(trimStats[i][0])
        print("ID: DIAMETER: RIM: SIZE:")
        print(str(trimStats[i]) + "\n")
    
    print("\n")
    input("Press Enter to return to the main menu...")
    project.baseMenu(_conn)

def moreInformation(conn):
    cursor = conn.cursor()

    while True:
        project.clear_screen()
        print("What would you like to see?")
        print("1. Filter cars")
        print("2. Sort cars")
        print("3. Manufacturer stats")
        print("4. Back\n")

        choice = input("Select an option: ").strip()

        if choice == '1':
            handle_car_filters(cursor)
        elif choice == '2':
            handle_car_sorting(cursor)
        elif choice == '3':
            manufacturer_stats(cursor)
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")
            input("\nPress Enter to continue...")

    project.baseMenu(conn)


def handle_car_filters(cursor):
    while True:
        project.clear_screen()
        print("How would you like to filter the cars?")
        print("1. By Year")
        print("2. By Make")
        print("3. By Cylinder Count")
        print("4. By Fuel Type")
        print("5. Back\n")

        filter_choice = input("Select a filter: ")

        try:
            if filter_choice == '1':
                filter_by_year(cursor)
            elif filter_choice == '2':
                filter_by_make(cursor)
            elif filter_choice == '3':
                filter_by_cylinders(cursor)
            elif filter_choice == '4':
                filter_by_fuel_type(cursor)
            elif filter_choice == '5':
                break
            else:
                print("Invalid option, please try again.")
        except Error as e:
            print("Database error:", e)

        input("\nPress Enter to continue...")

def filter_by_year(cursor):
    project.clear_screen()
    year = input("Enter the minimum year: ").strip()
    if not year.isdigit():
        print("Invalid year.")
        return

    cursor.execute(
        "SELECT c_model, c_year FROM car WHERE c_year > ?",
        (int(year),)
    )
    results = cursor.fetchall()
    print(f"\nCars from after year {year}:")
    for model, y in results:
        print(f"- {model} ({y})")

def filter_by_make(cursor):
    project.clear_screen()
    print("Available Makes:\n")
    cursor.execute("SELECT DISTINCT c_make FROM car ORDER BY c_make")
    makes = [row[0] for row in cursor.fetchall()]
    for m in makes:
        print(f"- {m}")

    make = input("\nEnter the make: ").upper().strip()
    if make not in makes:
        print("Invalid make selected.")
        return

    cursor.execute(
        "SELECT c_model, c_make FROM car WHERE c_make = ?",
        (make,)
    )
    results = cursor.fetchall()
    project.clear_screen()
    print(f"\nCars from make {make}:")
    for model, m in results:
        print(f"- {model} ({m})")

def filter_by_cylinders(cursor):
    project.clear_screen()
    cylinders = input("Enter the minimum number of cylinders: ").strip()
    if not cylinders.isdigit():
        print("Invalid cylinder count.")
        return

    cursor.execute(
        """
        SELECT DISTINCT c.c_model, e.e_cylinders
        FROM car c
        JOIN trim t ON c.c_model = t.t_model
        JOIN engine e ON t.t_engine = e.e_id
        WHERE e.e_cylinders >= ?
        """,
        (int(cylinders),)
    )
    results = cursor.fetchall()
    project.clear_screen()
    print(f"\nCars with at least {cylinders} cylinders:")
    for model, cyl in results:
        print(f"- {model} ({cyl} cylinders)")

def filter_by_fuel_type(cursor):
    project.clear_screen()
    print("Available Fuel Types:\n")
    cursor.execute("SELECT DISTINCT e_fuelType FROM engine ORDER BY e_fuelType")
    fuel_types = [row[0] for row in cursor.fetchall()]
    for f in fuel_types:
        print(f"- {f}")

    fuel_type = input("\nEnter the fuel type: ").upper().strip()
    if fuel_type not in fuel_types:
        print("Invalid fuel type selected.")
        return

    cursor.execute(
        """
        SELECT DISTINCT c.c_make, c.c_model, e.e_fuelType
        FROM car c
        JOIN trim t ON c.c_model = t.t_model
        JOIN engine e ON t.t_engine = e.e_id
        WHERE e.e_fuelType = ?
        """,
        (fuel_type,)
    )
    results = cursor.fetchall()
    project.clear_screen() 
    print(f"\nCars with fuel type {fuel_type}:")
    for make, model, fuel in results:
        print(f"- {make} {model} ({fuel})")

def manufacturer_stats(cursor):
    ## MANUFACTURER STATS FUNCTION ##
    project.clear_screen()
    print("Available Makes:\n")
    cursor.execute("SELECT DISTINCT c_make FROM car ORDER BY c_make")
    makes = [row[0] for row in cursor.fetchall()]
    for m in makes:
        print(f"- {m}")
    make = input("\nEnter the manufacturer to see stats: ").upper().strip()
    if make not in makes:
        print("Invalid manufacturer selected.")
        return
    project.clear_screen()
    print("What stats would you like to see?")
    print("1. Number of Models")
    print("2. Average MPG")
    print("3. Average Price")
    print("4. Back\n")
    stat_choice = input("Select a stat: ").strip()
    if stat_choice == '1':
        cursor.execute(
            "SELECT COUNT(DISTINCT c_model) FROM car WHERE c_make = ?",
            (make,)
        )
        result = cursor.fetchone()
        project.clear_screen()
        print(f"\nNumber of models by {make}: {result[0]}")
        input("\nPress Enter to continue...")
    elif stat_choice == '2':
        cursor.execute(
            """
            SELECT AVG(t.t_eco)
            FROM car c
            JOIN trim t ON c.c_model = t.t_model
            WHERE c.c_make = ?
            """,
            (make,)
        )
        result = cursor.fetchone()
        project.clear_screen()
        print(f"\nAverage MPG for {make}: {result[0]:.2f}")
        input("\nPress Enter to continue...")
    elif stat_choice == '3':
        cursor.execute(
            """
            SELECT AVG(t.t_price)
            FROM car c
            JOIN trim t ON c.c_model = t.t_model
            WHERE c.c_make = ?
            """,
            (make,)
        )
        result = cursor.fetchone()
        project.clear_screen()
        print(f"\nAverage Price for {make}: ${result[0]:.2f}")
        input("\nPress Enter to continue...")
    elif stat_choice == '4':
        return
    else:
        print("Invalid option selected.")

def handle_car_sorting(cursor):
    while True:
        project.clear_screen()
        print("How would you like to sort the cars?")
        print("1. By Minimum Price")
        print("2. By Maximum Horsepower")
        print("3. By Minimum Acceleration")
        print("4. Back\n")

        sort_choice = input("Select a sorting option: ")

        try:
            if sort_choice == '1':
                sort_by_price(cursor)
            elif sort_choice == '2':
                sort_by_horsepower(cursor)
            elif sort_choice == '3':
                sort_by_acceleration(cursor)
            elif sort_choice == '4':
                break
            else:
                print("Invalid option, please try again.")
        except Error as e:
            print("Database error:", e)

        input("\nPress Enter to continue...")

def sort_by_price(cursor):
    project.clear_screen()
    cursor.execute(
        """
        SELECT c.c_model, MIN(t.t_price) AS min_price
        FROM car c
        JOIN trim t ON c.c_model = t.t_model
        GROUP BY c.c_model
        ORDER BY min_price ASC
        """
    )
    results = cursor.fetchall()
    print("Cars sorted by Price (Lowest to Highest):")
    for model, price in results:
        print(f"- {model}: ${price}")

def sort_by_horsepower(cursor):
    project.clear_screen()
    cursor.execute(
        """
        SELECT c.c_model, MAX(e.e_horsepower) AS max_horsepower
        FROM car c
        JOIN trim t ON c.c_model = t.t_model
        JOIN engine e ON t.t_engine = e.e_id
        GROUP BY c.c_model
        ORDER BY max_horsepower DESC
        """
    )
    results = cursor.fetchall()
    print("Cars sorted by Horsepower (Highest to Lowest):")
    for model, horsepower in results:
        print(f"- {model}: {horsepower} HP")

def sort_by_acceleration(cursor):
    project.clear_screen()
    cursor.execute(
        """
        SELECT c.c_model, MIN(t.t_accel) AS best_acceleration
        FROM car c
        JOIN trim t ON c.c_model = t.t_model
        GROUP BY c.c_model
        ORDER BY best_acceleration ASC
        """
    )
    results = cursor.fetchall()
    print("Cars sorted by Acceleration (Fastest to Slowest 0-60):")
    for model, acceleration in results:
        print(f"- {model}: {acceleration} seconds")

        
    