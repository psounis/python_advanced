# pip install pytz
from pytz import timezone
from datetime import datetime

now = datetime.now()
# tz names: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
us_now = datetime.now(timezone("America/New_York"))
kt_now = datetime.now(timezone("Asia/Katmandu"))

print("Greece time: " + str(now))
print("US/New York time: " + str(us_now))
print("Katmandu time: " + str(kt_now))
