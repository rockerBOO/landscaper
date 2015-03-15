
import landscaper.properties.translate as translate
import json 
import landscaper.orm.config as config

import landscaper.orm.data as data
import landscaper.plant.plant as plant
import landscaper.properties.properties as properties
import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '.')

config.Set("datastore", "redis")
data.SetKey("PrairieMoonImport")

config.Set("pmap", "PrairieMoon")

def PropertyMap():
	return json.load(open("pmap/PrairieMoon"))
	
InputPlant = plant.Plant()
InputPlant.Properties = {"Height": ["5 ft."], "Sun Exposure": ["Full Sun", "Part Shade"]}
print(InputPlant.Properties)

Plant = translate.Translate(InputPlant, PropertyMap())

print(Plant.Properties)

plant.SavePlant(Plant)

#translate.SetPmap("pmap", )


#orm.data.SetDefaultKey("PrairieMoonImport")
