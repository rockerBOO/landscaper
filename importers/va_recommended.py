import json
import landscaper.web as web
from glob import glob
from pymongo import MongoClient


soup = web.soup(open('../data/bamona.html',encoding='iso-8859-1'))

aboutBlockRemoved = False

fields = []

results = []

for row in soup.find_all('tr'):
	# remove first td

	i = 0

	plant = {}

	for column in row.find_all('td'):
		if aboutBlockRemoved == False:
			aboutBlockRemoved = True
			continue

		if len(fields) != 6:
			fields.append(column.string.strip())
			continue

		column_length = len(column)

		if column_length == 3:
			name = column.contents[0].string.strip()
			ssp = column.contents[1].string.strip()
		elif column_length == 2:
			pass
		elif column_length == 1:
			print(column.string.strip())
			name = column.string.strip()
			#name = column.contents.strip()

		names = []

		for n in name.split(','):
			names.append(n.strip())

		plant[fields[i]] = names

		print(column.string)
		i += 1

	results.append(plant)

col = MongoClient().landscaper.va_plants

ids = col.insert(results)

print("Done.")
