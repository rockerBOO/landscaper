
import redis
from . import config

r = redis.StrictRedis(host='localhost', port=6379, db=0)

config.Set("redis-connection", r)

def redisConnection():
	return config.Get("redis-connection")

def redisGet(key):
	redisConnection().get(key)


def redisSet(key, value):
	#redisConnection().set(key, value)
	pass

def Get(key):
	if (config.Get("datasource") == "redis"):
		return redisGet(key)

def Set(key, value):
	if (config.Get("datastore") == "redis"):
		return redisSet(key, value)



def SetKey(key):
	global _dataKey

	_dataKey = key

def Key():
	global _dataKey

	return _dataKey