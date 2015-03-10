
from landscaper.plant import plant

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


def TranslateProperty(attribute, property, propertyMap):
	print("pmap attribute", attribute)

	if attribute in propertyMap.keys():
	    mappings = propertyMap[attribute]

	    for key in mappings.keys():
	        print("mapping", attribute, property, mappings)
	        if key == 'replace':
	            mapped.append(replace(property, mappings[key]))
	        elif key == 'match':
	            mapped.append(match(property, mappings[key]))
	        else:
	            print("key", key)


#input "2-3ft'"
#mappings "match": ["(?P<min>\\d+)-(?P<max>\\d+)"],
def match(properties, mappings):
    result = []

    for regex, mapping in mappings.items():
        print("regex", regex)

        try:
            mapMatches = re.findall(regex, input)
        except TypeError:
            print(TypeError)
            continue

        for group in mapMatches:
            matches = []

            print("mapMatches", mapMatches)

            for mm in mapMatches:
                for m in mm:
                    print("m", m)
                    matches.append(m)

            for x, y in [(x,y) for x in mapping for y in matches]:
                print("x:y", x, y)
                result.append({x: y})


    return result

#input ["Part Shade"]
#mappings {"Full Sun": {"Light": 10}, "Part Shade": {"Light":10}}
def replace(properties, mappings):
    result = []

    print("replace", input)

    for k, v in mappings.items():
        if isinstance(input, list):
            for value in input:
                if isinstance(v, dict):
                    if value == k:
                        result.append(v)

    return result


def Translate(InputPlant, propertyMap):
	translated = [TranslateProperty(attribute, property, propertyMap) 
		for attribute, property in InputPlant.Properties.items()]

	plant = Plant()

	for propertyList in translated:
		attribute = propertyList[0]
		property = propertyList[1]

		plant.SetProperty(attribute, property)


	return plant


