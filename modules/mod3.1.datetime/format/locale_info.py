from datetime import datetime
import locale

for loc in ['greek', 'french', 'german', 'italian']:
    print("Language: " + loc)
    locale.setlocale(locale.LC_TIME, loc)
    d=datetime.now()
    for i in range(1,8):
        print(d.replace(day=i).__format__(f"%A %d %B %Y"))
    print("="*10)
