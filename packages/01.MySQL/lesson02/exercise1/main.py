from dbtools import *
from country import Country

connector = open_connection()

try:
    c = Country(connector)
    while True:
        print("="*20)
        print("Menu (Current country: " + str(c.name) + ")")
        print("="*20)
        print("1-Load Country")
        print("2-Insert New Country")
        print("3-Update Country")
        print("4-Delete Country")
        print("5-Print Country")
        print("6-Save Country")
        print("7-Exit")
        choice = int(input("Your choice: "))
        if choice == 1:
            code = input("Give country code: ")
            c.load_country(code)
            if c.name is not None:
                c.print_country()
        elif choice == 2:
            c.insert_country()
        elif choice == 3:
            c.update_country()
        elif choice == 4:
            c.delete_country()
            c = Country(connector)
        elif choice == 5:
            c.print_country()
        elif choice == 6:
            c.save_country()
        else:
            break

except MYSQL.Error as e:
    print(e)

close_connection(connector)
