
import config
import data
import dataset
from collections import OrderedDict
import plant
import properties

config.Set("datastore", "redis")
data.SetKey("PrairieMoonImport")


def PlantList():
	keys = OrderedDict()

	for line in dataset.CSVFileDataset(open("data/plantlist", encoding='utf-8')):
		# CSV apply first line to the keys
		if len(keys) == 0:
			keys = line
			continue

		yield line

for plantList in PlantList():
	print(plantList)

	commonName = properties.TextProperty(plantList[3])
	scientificNamePlusAuthor = properties.TextProperty(plantList[2])
	family = properties.TextProperty(plantList[4])

	Plant = plant.Plant()

	Plant.addProperty("Name", commonName)
	Plant.addProperty("ScientificName", scientificNamePlusAuthor)
	Plant.addProperty("Family", family)

	plant.AddPlant(Plant)

	print(Plant.Properties)