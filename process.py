
import translate
import json 
import config

config.Set("datastore", "redis")

for attribute, mapping in json.load(open("pmap/PrairieMoon")).items():
	print(attribute)
	print(mapping)

translate.SetPmap("pmap", )

config.set("pmap", "PrairieMoon")

data.SetDefaultKey("PrairieMoonImport")


for inputPlant in plants:
	Plant = translate.Translate(inputPlant)

	plant.SavePlant(Plant)
