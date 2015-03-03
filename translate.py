#ImportedPlant 
#	ImportedProperties

#translated = map(translate, ImportedProperties)

#> save to translated database

_pmap = None

def GetPmap(key):
	global _pmap

	if isinstance(_pmap, None):
		# error
		pass

	return _pmap

def SetPmap(key, value):
	global _pmap

	_pmap = value
	config.Set("pmap", key)


def TranslateProperty(input):
	pmap = GetPmap(config.get("pmap"))

	

	return [attribute, property]


def Translate(InputPlant):
	translated = map(TranslateProperty, InputPlant.Properties)

	plant = Plant()

	for propertyList in translated:
		attribute = propertyList[0]
		property = propertyList[1]

		plant.addProperty(attribute, property)


	return plant


