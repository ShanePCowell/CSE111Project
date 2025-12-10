import sqlite3
from sqlite3 import Error

import project

def addVehicle(_conn):
    ## ADD VEHICLE FUNCTION ##
    print("Add Vehicle:")
    v_make = input("Enter Vehicle Make: ")
    v_model = input("Enter Vehicle Model: ")
    valid = False
    while valid==False:
        v_year = input("Enter Vehicle Year: ")
        if (not v_year.isdigit() or int(v_year) <= 0):
            print("Please Enter a Year.")
        else:
            valid=True
    v_bType = input("Enter Vehicle Body Type: ")
    valid = False
    while valid==False:
        v_wBase= input("Enter Vehicle Wheel Base: ")
        if (not v_wBase.isdigit() or int(v_wBase) <= 0):
            print("Please Enter a number.")
        else:
            valid=True
    try:
        _conn.execute(
            f'''INSERT INTO car(c_model, c_year, c_make, c_bodyType, c_wheelBase)
            VALUES ('{v_make}', '{v_model}', {v_year}, '{v_bType}', {v_wBase})'''
        )
        
    except Error as e:
        print(e)
        addVehicle(_conn)
        
     ## ADD TRIMS ##
    engines=[]
    transmissions=[]
    trims=[]
    wheel=[]
    valid = False
    while valid==False:
        tNum = input("Enter Number of Trims: ")
        if (not tNum.isdigit() or int(tNum) <= 0):
            print("Invalid number of trims. Try again.")
        else:
            valid=True
    tNum = int(tNum)
    for i in range(tNum):
        print(f"Trim {i+1}:")
        value = False
        while not value:
            try:
                t_name = input(" Enter Trim Name: ")
                t_price = int(input(" Enter Trim Price: "))
                t_mpg = int(input(" Enter Trim MPG: "))
                t_weight = int(input(" Enter Trim Weight: "))
                t_speed = int(input(" Enter Trim Top Speed: "))
                t_accel = int(input(" Enter Trim Acceleration: "))
                value = True
            except ValueError:
                print(" Invalid input. Please try again.")
        t_engine = input(" Enter Engine Name: ")
        t_transmission = input(" Enter Transmission Name: ")
        t_wheels = input(" Enter Wheels Name: ")
        if t_name not in trims:
            trims.append(t_name)
        if t_engine not in engines:
            engines.append(t_engine)
        if t_transmission not in transmissions:
           transmissions.append(t_transmission)
        if t_wheels not in wheel:
            wheel.append(t_wheels)
        try:
            _conn.execute(
                f'''INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
               VALUES ('{v_model}', '{t_name}', '{t_engine}', '{t_transmission}', '{t_wheels}', {t_accel}, {t_mpg}, {t_weight}, {t_speed}, {t_price})''')
        except Error as e:
            print(e)
            addVehicle(_conn)


    ## ADD ENGINES & TRANSMISSIONS ##
    for e in engines:
        value = False
        while not value:
            try:
                e_cylinders = int(input(f"Enter number of cylinders for engine {e}: "))
                e_layout = input(f"Enter layout for engine {e}: ")
                e_fuelType = input(f"Enter fuel type for engine {e}: ")
                e_displacement = float(input(f"Enter displacement for engine {e}: "))
                e_horsepower = int(input(f"Enter horsepower for engine {e}: "))
                e_torque = int(input(f"Enter torque for engine {e}: "))
                e_redline = int(input(f"Enter redline for engine {e}: "))
                value = True
            except ValueError:
                print(" Invalid input. Please try again.")
        for t in range(len(transmissions)):
            print(f"Transmission {t+1}: " + transmissions[t])
            valid = False
            while valid==False:
                trNum = input("Pick Transmission this Engine Uses: ")
                if (not trNum.isdigit() or int(trNum) > len(transmissions) or int(trNum) < 1):
                    print(len(transmissions))
                    print("Invalid input. Try again.")
                else:
                    valid=True

            try:
                _conn.execute(
                    f'''insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
                    VALUES ('{e}', {e_cylinders}, '{e_layout}', '{e_fuelType}', {e_displacement}, {e_horsepower}, {e_torque}, {e_redline})''')
                _conn.execute(
                   f'''insert into engine_Transmission(e_id, tr_id)   
                    Values ('{e}', '{transmissions[int(trNum)-1]}')''')
            except Error as e:
                print(e)
                addVehicle(_conn)
    
    for t in transmissions:
        value = False
        while not value:
            try:
                tr_type = input(f"Enter type for transmission {t}: ")
                tr_gears = int(input(f"Enter number of gears for transmission {t}: "))
                tr_driveType = input(f"Enter drive type for transmission {t}: ")
                tr_driveRatio = input(f"Enter final drive ratio for transmission {t}: ")
                value = True
            except ValueError:
                print(" Invalid input. Please try again.")

        try:
            _conn.execute(
                f'''INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
                VALUES ('{t}', {tr_gears}, {tr_driveRatio}, '{tr_driveType}', '{tr_type}')''')
        except Error as e:
            print(e)
            addVehicle(_conn)

    ## ADD WHEELS ##

    for w in wheel:
        value = False
        while not value:
            try:
                w_diameter = int(input(f"Enter diameter for wheels {w}: "))
                w_rim = input(f"Enter rim Type for wheels {w}: ")
                w_size = int(input(f"Enter rim size for wheels {w}: "))
                value = True
            except ValueError:
                print(" Invalid input. Please try again.")

        try:
            _conn.execute(
                f'''INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)
                VALUES ('{w}', {w_diameter}, '{w_rim}', {w_size})''')
        except Error as e:
            print(e)
            addVehicle(_conn)
    
    ## ADD COLORS ##
    valid = False
    while valid==False:
        cNum = input("Enter Number of Colors: ")
        if (not cNum.isdigit() or int(cNum) <= 0):
            print("Invalid number of colors. Try again.")
        else:
            valid=True
    cNum = int(cNum)
    for i in range(cNum):
        print(f"Color {i+1}:")
        c_name = input(" Enter Color Name: ")
        c_finish = input(" Enter Color Finish Type: ")
        c_color= input(" Enter Color (EG: RED, BLUE): ")
        try:
            _conn.execute(
                f'''INSERT INTO color(c_id, c_finish, c_color) VALUES ('{c_name}', '{c_finish}', '{c_color}')''')
        except Error as e:
            print(e)
            addVehicle(_conn)
        for i in range(tNum):
            t_name = input(f"Is this color used by trim ({trims[i]})? (y/n): ")
            if t_name.lower() == 'y':
                try:
                    _conn.execute(
                        f'''INSERT INTO color_Trim(c_id, t_id) VALUES ('{c_name}', '{trims[i]}')''')
                except Error as e:
                    print(e)
                    addVehicle(_conn)
    ## MANUFACTURER ##
    c=_conn.cursor()
    c.execute("SELECT m_make FROM manufacturer")
    row=c.fetchall()
    found = False
    for i in range(len(row)):
        if row[i][0]==v_make:
            found = True
    if not found:
        m_nation = input("Enter Manufacturer Country: ")
        try:
            _conn.execute(
                f'''INSERT INTO manufacturer(m_make, m_nationOfOrigin) VALUES ('{v_make}', '{m_nation}')''')
        except Error as e:
            print(e)
            addVehicle(_conn)
    _conn.commit()
    project.adminMenu(_conn)

def removeVehicle(_conn):
    print("Remove Vehicle:")
    c=_conn.cursor()
    c.execute("SELECT c_model FROM car")
    row=c.fetchall()
    for i in range(len(row)):
        print(f"Vehicle '{i+1}': " +  row[i][0])
    valid = False
    while valid==False:
        vNum = input("Select Car to Delete: ")
        if (not vNum.isdigit() or int(vNum) > len(row) or int(vNum) < 1):
            print("Invalid Option")
            project.adminMenu(_conn)
        else:
            valid=True
    try:
        _conn.execute(
            f'''DELETE FROM car WHERE c_model = '{row[int(vNum)-1][0]}' '''
        )
        _conn.commit()
    except Error as e:
        print(e)
    project.adminMenu(_conn)

def updateVehicle(_conn):
    print("Update Trim Price:")
    c=_conn.cursor()
    c.execute("SELECT t_model, t_id FROM trim")
    row=c.fetchall()
    for i in range(len(row)):
        print(f"Vehicle '{i+1}': " +  row[i][0] +  row[i][1])
    valid = False
    while valid==False:
        vNum = input("Select Trim to Edit: ")
        if (not vNum.isdigit() or int(vNum) > len(row) or int(vNum) < 1):
            print("Invalid Option")
            project.adminMenu(_conn)
        else:
            valid=True
    value = False
    while not value:
        try:
            newPrice = int(input("Enter New Price: "))
            value = True
        except ValueError:
            print(" Invalid input. Please try again.")
    try:
        _conn.execute(
            f'''UPDATE trim SET t_price = '{newPrice}' WHERE t_model = '{row[int(vNum)-1][0]}' AND t_id = '{row[int(vNum)-1][1]}' '''
        )
        _conn.commit()
    except Error as e:
        print(e)
    project.adminMenu(_conn)