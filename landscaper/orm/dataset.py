import csv

def Dataset(dataset):
	pass

def GetDataset(dataset):
	for line in dataset:
		yield line


def CSVFileDataset(file):
	try:
		for line in csv.reader(file):
			yield line
	except UnicodeDecodeError:
		print("Decode error with "+ line)
		yield []
		

def FileDataset(file):
	for line in open(file).readlines():
		# convert data
		yield line

