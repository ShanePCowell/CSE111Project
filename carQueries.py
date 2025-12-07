import sqlite3
from sqlite3 import Error

import project

def compareVehicles(_conn):
    ## COMPARE VEHICLES FUNCTION ##
    c=_conn.cursor()
    c.execute("SELECT c_model FROM car")
    row=c.fetchall()
    for i in range(len(row)):
        print(f"Vehicle '{i+1}': " +  row[i][0])    
    value = False
    while not value:
        try:
            v1 = int(input("Select First Vehicle to Compare: "))
            v2 = int(input("Select Second Vehicle to Compare: "))
            value = True
        except ValueError:
            print(" Invalid input. Please try again.")

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

    print("\n \n")

    project.baseMenu(_conn)

def SeeStats(_conn):
    ## SEE STATS FUNCTION ##
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

    c.execute(f"SELECT e_id, e_horsepower, e_torque, e_redline, e_fuelType, e_cylinders, e_displacement FROM engine JOIN trim on e_id=t_engine WHERE t_model = '{row[v1-1][0]}'")
    trimStats=c.fetchall()
    for i in range(len(trimStats)):
        print("Engine for Trim " + str(i+1))
        print("ID: HORSEPOWER: TORQUE: REDLINE: FUELTYPE: CYLINDERS: DISPLACEMENT:")
        print(str(trimStats[i]) + "\n")
    
    c.execute(f"SELECT tr_id, tr_type, tr_gears, tr_driveType, tr_driveRatio FROM transmission JOIN trim on tr_id=t_transmission WHERE t_model = '{row[v1-1][0]}'")
    trimStats=c.fetchall()
    for i in range(len(trimStats)):
        print("Transmission for Trim " + str(i+1))
        print("ID: TYPE: GEARS: DRIVETYPE: DRIVERATIO:")
        print(str(trimStats[i]) + "\n")
    
    c.execute(f"SELECT w_id, w_diameter, w_rim, w_size FROM wheel JOIN trim on w_id=t_wheels WHERE t_model = '{row[v1-1][0]}'")
    trimStats=c.fetchall()
    for i in range(len(trimStats)):
        print("Wheels for Trim " + str(i+1))
        print("ID: DIAMETER: RIM: SIZE:")
        print(str(trimStats[i]) + "\n")