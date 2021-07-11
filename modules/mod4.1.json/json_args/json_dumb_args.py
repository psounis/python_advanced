import decimal
import json

with open("ob.json", "r") as f:
    person = json.load(f, parse_int=decimal.Decimal,
                       parse_float=decimal.Decimal)
    print(person)