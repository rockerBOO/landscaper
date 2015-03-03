

# Reduce plant list
def Assemble(plants):

	resultPlant = Plant()

	for plant in plants:
		for attribute, property in plant.Properties.items():
			resultPlant.AddProperty(attribute, property)


	return resultPlant
