from django.shortcuts import render,render_to_response,HttpResponse
from app.src.CONST import *
from app.src.coon_redis import get_rcoon
import json
# Create your views here.
def index(req):
	return render_to_response('index.html',{'keys':KEYS})
def get_value(req):
	key = req.POST.get('key')
	key_type = KEYS[key]
	r_coon = get_rcoon()
	print(r_coon.get(key))
	if key_type=='str':
		data = r_coon.get(key)
	else:
		data = json.dumps(r_coon.hgetall(key))
	return HttpResponse(data)
def del_key():
	# key = req.POST.get('key')
	key = 'ad.nadp.consume'
	v = 1
	r_coon = get_rcoon()
	print r_coon.hdel(key,v)

# del_key()
