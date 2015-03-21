


cursor = db.connect("server=localhost user=rockerboo")

processingJob = data.get('processing-job')

query = "select * from list where job_id = 1"

cur.select(query)


propertyMap = property.map(json.decode(open('./pmap/PrairieMoon')))

processor = Processor()

# Hook on finish
processor.finish = lambda (key):
	processedKey = 'processed-'

	processor.add(key)

# Hook on start
processor.start = lambda (key):
	pass 

processor.work = lambda (key):
	properties = data.get(key)

	Plant.import(properties, propertyMap)

	processedKey = 'processed-'

	data.save(processedKey, Plant.toData())

for key in dataList:
	processor.do(key)

