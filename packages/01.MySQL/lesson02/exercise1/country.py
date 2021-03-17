from dbtools import *


class Country:
    def __init__(self, connector):
        self.code = None
        self.name = None
        self.continent = None
        self.region = None
        self.surface_area = None
        self.indep_year = None
        self.population = None
        self.life_expectancy = None
        self.gnp = None
        self.gnp_old = None
        self.local_name = None
        self.government_form = None
        self.head_of_state = None
        self.capital = None
        self.code2 = None
        self.connector = connector

    def __str__(self):
        return f"{self.name} ({self.region}, {self.continent})"

    def load_country(self, code):
        results = query_full_results(self.connector,
                                     "SELECT * FROM country WHERE Code='" + code + "'")

        if results:
            data = results[0]
            self.code = data["Code"]
            self.name = data["Name"]
            self.continent = data["Continent"]
            self.region = data["Region"]
            self.surface_area = data["SurfaceArea"]
            self.indep_year = data["IndepYear"]
            self.population = data["Population"]
            self.life_expectancy = data["LifeExpectancy"] if data["LifeExpectancy"] is not None else None
            self.gnp = data["GNP"] if data["GNP"] is not None else None
            self.gnp_old = data["GNPOld"] if data["GNPOld"] is not None else None
            self.local_name = data["LocalName"]
            self.government_form = data["GovernmentForm"]
            self.head_of_state = data["HeadOfState"] if data["HeadOfState"] is not None else None
            self.capital = data["Capital"] if data["Capital"] is not None else None
            self.code2 = data["Code2"]
        else:
            print("No such code. ")

    def save_country(self):
        if self.code is not None:
            query = "UPDATE country "
            query += "SET "
            query += " Code = '" + self.code + "',"
            query += " Name = '" + self.name + "',"
            query += " Continent = '" + self.continent + "',"
            query += " Region = '" + self.region + "',"
            query += " SurfaceArea = " + str(self.surface_area) + ","
            if self.indep_year is None:
                query += " IndepYear = NULL, "
            else:
                query += " IndepYear = " + str(self.indep_year) + ","
            query += " Population = " + str(self.population) + ","
            if self.life_expectancy is None:
                query += " LifeExpectancy = NULL, "
            else:
                query += " LifeExpectancy = " + str(self.life_expectancy) + ", "
            if self.gnp is None:
                query += " GNP = NULL, "
            else:
                query += " GNP = " + str(self.gnp) + ", "
            if self.gnp_old is None:
                query += " GNPOld = NULL, "
            else:
                query += " GNPOld = " + str(self.gnp_old) + ", "
            query += " LocalName = '" + self.local_name + "', "
            query += " GovernmentForm = '" + self.government_form + "', "
            if self.head_of_state is None:
                query += " HeadOfState = NULL, "
            else:
                query += " HeadOfState = '" + self.head_of_state + "', "
            if self.capital is None:
                query += " Capital = NULL, "
            else:
                query += " Capital = " + str(self.capital) + ", "
            query += " Code2 = '" + self.code2 + "' "
            query += " WHERE Code='" + self.code + "'"
            update_query(self.connector, query)
            self.connector.commit()
            print("Country is saved.")
        else:
            print("Cannot update. Country is not initialized!")

    def insert_country(self):
        print("Insert new country:")
        self.code = input("Give code: ")
        query="SELECT * FROM country WHERE code ='" + self.code + "'"
        results = query_full_results(self.connector, query)
        if results:
            print("Code already exists!")
            return

        self.name = input("Give name: ")
        self.continent = input("Give continent: ")
        self.region = input("Give region: ")
        self.surface_area = input("Give surface area: ")
        inp = input("Give independence year (type None if unknown): ")
        if inp == "None":
            self.indep_year = None
        else:
            self.indep_year = int(inp)
        self.population = int(input("Give population: "))
        inp = input("Give life expectancy (type None if unknown): ")
        if inp == "None":
            self.life_expectancy = None
        else:
            self.life_expectancy = float(inp)
        inp = input("Give GNP (type None if unknown): ")
        if inp == "None":
            self.gnp = None
        else:
            self.gnp = float(inp)
        inp = input("Give GNPold (type None if unknown): ")
        if inp == "None":
            self.gnp_old = None
        else:
            self.gnp_old = float(inp)
        self.local_name = input("Give local name: ")
        self.government_form = input("Give government form: ")
        inp = input("Give head of state (type None if unknown): ")
        if inp == "None":
            self.head_of_state = None
        else:
            self.head_of_state = inp
        inp = input("Give capital (type None if unknown): ")
        if inp == "None":
            self.capital = None
        else:
            self.capital = inp
        self.code2 = input("Give Code2: ")

        query = "INSERT INTO country "
        query += "VALUES ("
        query += " '" + self.code + "',"
        query += " '" + self.name + "',"
        query += " '" + self.continent + "',"
        query += " '" + self.region + "',"
        query += " " + str(self.surface_area) + ","
        if self.indep_year is None:
            query += " NULL, "
        else:
            query += " " + str(self.indep_year) + ","
        query += " " + str(self.population) + ","
        if self.life_expectancy is None:
            query += " NULL, "
        else:
            query += " " + str(self.life_expectancy) + ", "
        if self.gnp is None:
            query += " NULL, "
        else:
            query += " " + str(self.gnp) + ", "
        if self.gnp_old is None:
            query += " NULL, "
        else:
            query += " " + str(self.gnp_old) + ", "
        query += " '" + self.local_name + "', "
        query += " '" + self.government_form + "', "
        if self.head_of_state is None:
            query += " NULL, "
        else:
            query += " '" + self.head_of_state + "', "
        if self.capital is None:
            query += " NULL, "
        else:
            query += " " + str(self.capital) + ", "
        query += " '" + self.code2 + "' "
        query += ")"
        insert_query(self.connector, query)
        self.connector.commit()
        print("Country is saved.")



    def update_country(self):
        if self.code is None:
            print("First, choose a country")
            return

        while True:
            print("Country update: ")
            print("1-code")
            print("2-name")
            print("3-continent")
            print("4-region")
            print("5-surface area")
            print("6-independence year")
            print("7-population")
            print("8-life expectancy")
            print("9-GNP")
            print("10-GNP old")
            print("11-Local Name")
            print("12-Government Form")
            print("13-Head of State")
            print("14-Capital")
            print("15-Code2")
            print("16-exit")
            choice = int(input("Pick one: "))
            if choice == 1:
                self.code = input("Give new code: ")
            elif choice == 2:
                self.name = input("Give new name: ")
            elif choice == 3:
                self.continent = input("Give new continent: ")
            elif choice == 4:
                self.region = input("Give new region: ")
            elif choice == 5:
                self.surface_area = float(input("Give new surface area: "))
            elif choice == 6:
                self.indep_year = int(input("Give new independence year: "))
            elif choice == 7:
                self.population = int(input("Give new population: "))
            elif choice == 8:
                self.life_expectancy = float(input("Give new life expectancy: "))
            elif choice == 9:
                self.gnp = float(input("Give new GNP: "))
            elif choice == 10:
                self.gnp_old = float(input("Give new GNPold: "))
            elif choice == 11:
                self.local_name = input("Give new local name: ")
            elif choice == 12:
                self.government_form = input("Give new government form: ")
            elif choice == 13:
                self.head_of_state = input("Give new head of state: ")
            elif choice == 14:
                self.capital = input("Give new capital: ")
            elif choice == 15:
                self.code2 = input("Give new Code2: ")
            else:
                break

    def delete_country(self):
        if self.code is None:
            print("No country selected!")
        else:
            query = "DELETE FROM country WHERE code='" + self.code + "'"
            delete_query(self.connector, query)
            self.connector.commit()
            print("Country is deleted!")

    def print_country(self):
        if self.code is None:
            print("First, choose a country")
            return

        print("=" * 35)
        print(f"Code: {self.code}")
        print(f"Name: {self.name}")
        print(f"Continent: {self.continent}")
        print(f"Region: {self.region}")
        print(f"Surface Area: {self.surface_area}")
        print(f"Independence Year: {self.indep_year}") if self.indep_year is not None else print("Independence Year: (no value)")
        print(f"Population: {self.population}")
        print(f"Life Expectancy: {self.life_expectancy}") if self.life_expectancy is not None else print("Life Expectancy: (no value)")
        print(f"GNP: {self.gnp}") if self.gnp is not None else print("GNP: (no value)")
        print(f"GNPold: {self.gnp_old}") if self.gnp_old is not None else print("GNPold: (no value)")
        print(f"Local Name: {self.local_name}")
        print(f"Government Form: {self.government_form}")
        print(f"Head of State: {self.head_of_state}") if self.head_of_state is not None else print("Head of State: (no value)")
        print(f"Capital: {self.capital}") if self.capital is not None else print("Capital: (no value)")
        print(f"Code2: { self.code2}")


