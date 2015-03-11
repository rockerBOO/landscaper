_config = {}

def Get(key):
	global _config

	return _config[key]

def Set(key, value):
	global _config

	_config[key] = value
