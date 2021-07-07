import csv
from os import name  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    #Cleaning redundant entires from db
    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    #Adding data to db
    for row in reader:
        #print(row)
        name = row[0]
        descp = row[1]
        just = row[2]
        
        try:
            year = int(row[3])
        except:
            year =None

        lat = float(row[4])
        long = float(row[5])
        
        try:
            area = float(row[6])
        except:
            area =None
        print('area',area)
        #print(name, descp, just, year, lat, long, area)
        
        cat, created = Category.objects.get_or_create(name=row[7])
        stat, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        data_head = Site(name=name, description=descp, justification=just,
                    year=year, latitude=lat, longitude=long, area_hectares=area, category_id=cat.id,
                    state_id=stat.id, region_id=reg.id, iso_id=iso.id)
        
        data_head.save()
        