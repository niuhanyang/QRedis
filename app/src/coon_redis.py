import redis
from app.src.CONST import *
coon = redis.Redis(host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWD)
def get_rcoon():
	# print coon.hgetall('ad.nadp.consume')
	# print coon.hget('ad.nadp.consume','')
	return coon
get_rcoon()