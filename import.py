
import landscaper.orm.config as config
import landscaper.orm.data as data
import landscaper.orm.dataset as dataset
from collections import OrderedDict
import landscaper.plant

import landscaper.processors.usda as usda

import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '.')

config.Set("datastore", "redis")
data.SetKey("PrairieMoonImport")


def PlantList():
	keys = OrderedDict()

	for line in dataset.CSVFileDataset(open("data/plantlist", encoding='utf-8')):
		# CSV apply first line to the keys
		if len(keys) == 0:
			keys = line
			continue

		yield keys, line


for keys, plantList in PlantList():
	print(plantList)
	print(keys)

	result = {}

	for index, key in enumerate(keys):
		result[key] = plantList[index]


	Plant = usda.USDA.ImportProperties(result)

	print(Plant.Properties)

	#plant.AddPlant(Plant)

	#print(Plant.Properties)