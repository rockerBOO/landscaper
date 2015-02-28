
import translate

config.set("datastore", "redis")

data.SetKey("PrairieMoonImport")

def translatePlant(data)
	pass

dataset = map(translatePlant, plants)

for plant in dataset:
