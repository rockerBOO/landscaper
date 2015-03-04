

def ProcessProperties(properties):
	commonName = properties.TextProperty(plantList[3])
	scientificNamePlusAuthor = properties.TextProperty(plantList[2])
	family = properties.TextProperty(plantList[4])

	Plant = plant.Plant()

	Plant.addProperty("Name", commonName)
	Plant.addProperty("ScientificName", scientificNamePlusAuthor)
	Plant.addProperty("Family", family)

	return Plant

def pmap():


