

# Reduce plant list
def Assemble(plants):

	resultPlant = Plant()

	for plant in plants:
		for attribute, property in plant.Properties.items():
			resultPlant.addProperty(attribute, property)


	return resultPlant
