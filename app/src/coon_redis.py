import redis
from app.src.CONST import *
def get_rcoon():
	coon = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWD)
	return coon
get_rcoon()