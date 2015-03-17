
from landscaper.plant import plant
import re
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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#input "2-3ft'"
#mappings "match": ["(?P<min>\\d+)-(?P<max>\\d+)"],
def match(properties, mappings):
	results = []

	for regex, mapping in mappings.items():
		for property in properties:
			print("match_property", property, regex, mapping)

			result = match_property(property, regex, mapping)
			results.append(result)

	return results

def match_property(property, regex, map):
	print("match_property", property, regex, map)

	try:
		match = re.findall(regex, property)
	except TypeError:
		print(TypeError)
		return

	if match:
		print('da match', match)
		for group in match:
			matches = []

			print("match", match)

			for mm in match:
				for m in mm:
					print("m", m)
					matches.append(m)

			for x, y in [(x,y) for x in map for y in matches]:
				print("x:y", x, y)
				return {x: y}

	else:
		print("No matches found for this property. ", property)

def replace_property(attribute, property, map):
	if isinstance(input, list):
		for value in input:
			if isinstance(v, dict):
				if value == k:
					return v



#input ["Part Shade"]
#mappings {"Full Sun": {"Light": 10}, "Part Shade": {"Light":10}}
def replace(properties, mappings):
	result = []

	print("replace", properties, mappings)

	for property in properties:
		print(property)


	return result

def TranslateProperty(attribute, properties, propertyMap):
	print("pmap attribute", attribute)
	print("propertyMap", propertyMap)

	results = []

	# Find attribute in property map
	if attribute in propertyMap.keys():
		mappings = propertyMap[attribute]

		# Loop through property map's mappings for the attribute
		for key in mappings.keys():
			print("mapping", attribute, properties, mappings)


			if key == 'replace':

				return replace(properties, mappings[key])

			elif key == 'match':

				return match(properties, mappings[key])

			else:
				print("key", key)

	return results

# properties > translate > properties

def Translate(InputPlant, propertyMap):
	translated = [TranslateProperty(attribute, property, propertyMap) 
		for attribute, property in InputPlant.Properties.items()]

	print("translated", translated)



	if len(translated) == 0:
		print("No results translated.")
		return Plant

	print(translated)

	Plant = plant.Plant()

	# Loop through translated properties to apply to a Plant
	for properties in translated:
		print(properties)

		if len(properties) == 0:
			continue

		for p in properties:
			for attribute, property in p.items():

				Plant.SetProperty(attribute, property)

	print(Plant.Properties)

	return Plant


