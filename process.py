
import properties.translate as translate
import json 
import config
import orm.data
import plant

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '.')

#config.Set("datastore", "redis")


config.Set("pmap", "PrairieMoon")

def PropertyMap():
	return json.load(open("pmap/PrairieMoon"))
	
InputPlant = plant.Plant()

Plant = translate.Translate(InputPlant, PropertyMap())
plant.SavePlant(Plant)

#translate.SetPmap("pmap", )


#orm.data.SetDefaultKey("PrairieMoonImport")
