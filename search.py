
from elasticsearch import Elasticsearch

es = Elasticsearch()

query = {
  	"query": {
		"bool": {
		  	"must": [
				{ 
					"match": {
						"Sun": {'query': "Sun"}
					}
				},
				{ "match": {"Sun":  "Part-Shade"}},

				{ "match": {"Water": "Moist"}},
				{ "match": {"Water": "Dry"}},
		  	]
		}
	}
}

results = es.search(index="landscaper", doc_type="wildflowerorg", body=query)


# print(results[''])

plants = []

for hit in results['hits']['hits']:

	data = {
		'cnames': hit['_source']['Common Name'],
		'habits': hit['_source']['Habit'],
		'sun': hit['_source']['Sun'],
		'snames': hit['_source']['Scientific Name'],
		'water': hit['_source']['Water'],
	}

	plants.append(data)
	
	print(data)

	print(hit['_score'])

	print('__')

print(plants)

for plant in plants:
	print(plant['cnames'])
	print(plant['snames'])