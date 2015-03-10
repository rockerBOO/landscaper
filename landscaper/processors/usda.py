
import properties.properties as prop
import plant

class USDA:

	def ImportProperties(input, Plant=None):
		properties = {}

		for key, value in input.items():
			properties[key] = prop.TextProperty(value)

		if Plant == None:
			Plant = plant.Plant()

		Plant.SetProperties(properties)

		return Plant

	def TranslateImportedProperties(input):
		pmap = PropertyMap(self.PropertyMap())

		for key, value in input.items():
			pass

	def PropertyMap(self):
		return json.load(open("../pmap/PrairieMoon"))



class PropertyMap:
	def Set(value):
		self.data = value
