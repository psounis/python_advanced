import decimal
import json

with open("ob.json", "w") as f:
    json.dump([1,2,3,4.0,5.0], f, indent=2)

with open("ob.json", "r") as f:
    x = json.load(f, parse_int=decimal.Decimal,
                  parse_float=decimal.Decimal)