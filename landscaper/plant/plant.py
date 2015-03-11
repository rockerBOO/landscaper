
from ..orm import data as data

class Plant:
	Properties = {}

	def __init__(self, name=""):
		self.name = name

	def Name(self):
		if "Name" in self.Properties.keys():
			return self.Properties["Name"].Value()

		return ""

	def SetProperty(self, attribute, property):
		self.Properties[attribute] = property

	def SetProperties(self, properties):
		for attribute, property in properties.items():
			self.Properties[attribute] = property

def AddPlant(Plant):
	key = Plant.Name()

	return SavePlant(key, Plant)

def SavePlant(Plant):
	properties = {}

	for attribute, property in Plant.Properties.items():
		properties[attribute] = property.ToJSON()

	setResult = data.Set(data.Key() + Plant.Name(), {"Properties": properties})

	if setResult == False:
		# throw error
		print("Could not set the key (%s) to the datastore" % (Key() + key))


def GetPlant(key):
	data = data.Get(key)

	Plant = Plant()

	for attribute, property in data["Properties"].items():
		Plant.SetProperty(attribute, property.data)

	return Plant

def GetPlantList(key):
	list = data.Get(Key+"-list")

	for item in list:
		plant = data.Get(item)

		yield plant
