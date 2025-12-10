import sqlite3
from sqlite3 import Error

import os
import admin
import carQueries

loggedIn = True

def openConnection(_dbFile):

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
    except Error as e:
        print(e)
        print("failure")
    return conn

def closeConnection(_conn, _dbFile):

    try:
        _conn.close()
    except Error as e:
        print(e)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def adminMenu(conn):
    global loggedIn
    inputVal = ''  
    if not loggedIn:
        inputVal = input("\n Enter Admin Password: ")
    if (inputVal == 'admin' or loggedIn):
        loggedIn = True
        clear_screen()
        print("\n Admin Access Granted")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Update Vehicle")
        print("4. Exit Admin Menu")
        adminChoice = input()
        if adminChoice == '1':
            print("Add Vehicle selected")
            admin.addVehicle(conn)
        elif adminChoice == '2':
            print("Remove Vehicle selected")
            admin.removeVehicle(conn)
        elif adminChoice == '3':
            print("Update Vehicle selected")
            admin.updateVehicle(conn)
        elif adminChoice == '4':
            print("Exiting Admin Menu...")
            baseMenu(conn)
        else:
            print("Invalid option, please try again.")
            adminMenu(conn)
    else:
        print("Incorrect Password")
        baseMenu()
    

def baseMenu(conn):
    clear_screen()
    print("Car Comparison Tool")
    print("1. Compare Vehicles")
    print("2. See Vehicle Stats")
    print("3. More Information")
    print("4. Admin Tools")
    print("5. Exit \n")
    inputVal = input()
    if inputVal == '1':
        print("Compare Vehicles selected")
        carQueries.compareVehicles(conn)
    elif inputVal == '2':
        print("See Stats selected")
        carQueries.SeeStats(conn)
    elif inputVal == '3':
        print("More Information selected")
        carQueries.moreInformation(conn)
    elif inputVal == '4':
        adminMenu(conn)
    elif inputVal == '5':
        print("Exiting...")
    else:
        print("Invalid option, please try again.")
        baseMenu()

def main():
    global loggedIn
    database = r"cars.sqlite" # DELETED "CSE111Project/"

    loggedIn=True

    # create a database connection
    conn = openConnection(database)
    with conn:
        baseMenu(conn)


    closeConnection(conn, database)


if __name__ == '__main__':
    main()
