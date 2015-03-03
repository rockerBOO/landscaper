

import config
import data
import plant

plantList = plant.GetPlantList(key="PrairieMoonTranslated")



for plant in plantList:
	plant.GetPlant(plant)

# Reduce plant list
def Assemble(plants):

	resultPlant = Plant()

	for plant in plants:
		for attribute, property in plant.Properties.items():
			resultPlant.AddProperty(attribute, property)


	return resultPlant
