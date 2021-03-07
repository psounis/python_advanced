from dbtools import *


def continent_cities_countries(continent):
    query_cnt = "SELECT name, code FROM country WHERE continent='" + continent + "'"
    rows_countries = query_full_results(connector, query_cnt)

    if len(rows_countries) > 0:
        for row_country in rows_countries:
            query_cit = "SELECT name FROM city WHERE countryCode='" + row_country["code"] + "'"
            row_cities = query_full_results(connector, query_cit)
            print(row_country["name"] + "(" + ", ".join([cityd["name"] for cityd in row_cities]) + ")")
    else:
        print("No such continent (" + continent + ")")


connector = open_connection()

continent_cities_countries('Europe')

close_connection(connector)
