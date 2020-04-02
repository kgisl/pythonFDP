'''
The website that was scraped - https://www.sih.gov.in/finalResult
CSV file was generated using artoo.js and using the following JS snippet:

clist = artoo.scrapeTable('tbody', {
 header: 'first',
 done: artoo.saveCsv
});

'''

# https://docs.python.org/3.6/library/csv.html?highlight=csv%20file%20read#module-contents

import pprint
import csv
from collections import defaultdict

db = defaultdict(int)
cdb = defaultdict(list)

company = 'junk'
with open('sih.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')  # , quotechar = "|")
    for row in spamreader:
        cname = row[len(row) - 2]
        if len(row) == 7:
            company = row[0]
        if cname not in cdb[company]:
            cdb[company].append(cname)
        db[cname] += 1

print("number of colleges: ", len(db))

# https://docs.python.org/3/library/pprint.html#module-pprint
pp = pprint.PrettyPrinter(indent=4)

print("Top 10% colleges with maximum number of teams")
print("-----------------------------------")
dbsort = sorted(db.items(), key=lambda x: x[1], reverse=True)
pp.pprint(dbsort[:55])

print()
print("TOP COMPANIES with maximum colleges")
print("-----------------------------------")
cdbsort = sorted(cdb.items(), key=lambda x: len(x[1]), reverse=True)
print("total count:", len(cdbsort))
pp.pprint(cdbsort[1:11])

print()
print("College associated with KGISL")
print("-----------------------------------")
collegelist = sorted(cdb['KG Infosystem Pvt. Ltd.'],
                     key=lambda x: db[x], reverse=True)
print("total count:", len(collegelist))

for c in collegelist:
    print(c[:50], db[c])

print("\nISRO colleges-------------")
collegelist = sorted(cdb['ISRO'],
                     key=lambda x: db[x], reverse=True)
print("total count:", len(collegelist))

for c in collegelist:
    print(c[:50], db[c])
