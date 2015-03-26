
from elasticsearch import Elasticsearch

es = Elasticsearch()

results = es.search(index="landscaper", body={"query": {"match": {'Habit': 'Tree'}}})

print(results['hits']['hits'])

plants = []

for hit in results['hits']['hits']:

	plants.append({
		'cnames': hit['_source']['Common Name'],
		'habits': hit['_source']['Habit'],
		'sun': hit['_source']['Sun'],
		'snames': hit['_source']['Scientific Name'],
	})
	
	print()
	print('__')

print(plants)