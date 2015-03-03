
import data

class Plant:
	Properties = {}

	def __init__(self, name=""):
		self.name = name

	def Name(self):
		if "Name" in self.Properties.keys():
			return self.Properties["Name"].Value()

	def AddProperty(self, attribute, property):
		self.Properties[attribute] = property


def AddPlant(Plant):
	key = Plant.Name()

	return SavePlant(key, Plant)

def SavePlant(key, Plant):
	properties = {}

	for attribute, property in Plant.Properties.items():
		properties[attribute] = property.ToJSON()

	setResult = data.Set(data.Key() + key, {"Properties": properties})

	if setResult == False:
		# throw error
		print("Could not set the key (%s) to the datastore" % (Key() + key))


def GetPlant(key):
	data = data.Get(key)

	Plant = Plant()

	for attribute, property in data["Properties"].items():
		Plant.AddProperty(attribute, property.data)

	return Plant
