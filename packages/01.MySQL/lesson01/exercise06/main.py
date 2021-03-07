from dbtools import *


def print_country(country):
    print("="*35)
    print(f"Code: {country['Code']}")
    print(f"Name: {country['Name']}")
    print(f"Continent: {country['Continent']}")
    print(f"Region: {country['Region']}")
    print(f"Surface Area: {country['SurfaceArea']}")
    print(f"Independence Year: {country['IndepYear']}")
    print(f"Population: {country['Population']}")
    print(f"Life Expectancy: {country['LifeExpectancy']}")
    print(f"GNP: {country['GNP']}")
    print(f"GNPold: {country['GNPOld']}")
    print(f"Local Name: {country['LocalName']}")
    print(f"Government Form: {country['GovernmentForm']}")
    print(f"Head of State: {country['HeadOfState']}")
    print(f"Capital: {country['Capital']}")
    print(f"Code2: {country['Code2']}")


connector = open_connection()

try:
    # build query
    where_continent = ""
    print("Criterion 1: Continent")
    print("1-Specify continent")
    print("2-Don't specify continent")
    choice = int(input("Your choice: "))
    if choice == 1:
        continent = input("Give continent: ")
        where_continent = " Continent='" + continent + "' "

    where_indep_year = ""
    print("Criterion 2: Independence Year")
    print("1-Specify independence year")
    print("2-Don't specify independence year")
    choice = int(input("Your choice: "))
    if choice == 1:
        year_from = int(input("From Year: "))
        year_to = int(input("To Year: "))
        where_indep_year = " IndepYear BETWEEN " + str(year_from) + " AND " + str(year_to) + " "

    where_head_of_state = ""
    print("Criterion 3: Head of State")
    print("1-Specify head of state")
    print("2-Don't specify head of state")
    choice = int(input("Your choice: "))
    if choice == 1:
        governor = input("Give part(or whole)name of head of state: ")
        where_head_of_state = " HeadOfState LIKE '%" + str(governor) + "%' "

    list_clauses = []
    if len(where_continent) > 0:
        list_clauses.append(where_continent)
    if len(where_indep_year) > 0:
        list_clauses.append(where_indep_year)
    if len(where_head_of_state) > 0:
        list_clauses.append(where_head_of_state)
    where_clause = " AND ".join(list_clauses)
    if len(where_clause) > 0:
        where_clause = "WHERE " + where_clause

    query = "SELECT * FROM country " + where_clause

    iter_query = query_iter_many(connector, 5, query)

    for countries in iter_query:
        for country in countries:
            print_country(country)
        print("="*10 + ". Next? Press Enter...", end="")
        input()

except MYSQL.Error as e:
    print(e)

close_connection(connector)
