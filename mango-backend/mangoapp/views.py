from mangoapp.models import User, List
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json as simplejson

import pdb

@csrf_exempt
def add_user(request):

	response={}
	if request.method == 'POST':
		print request.POST
		try:
			uid = request.POST['uid']
			token = request.POST['token']
		except BaseException:
			uid = 0
			token = ''
		if not User.objects.filter(id=uid, access_token=token):
			if uid != 0:
				User.objects.create(id=uid, access_token=token)
				response.update({'response':'user added'})
			else:
				response.update({'response':'error'})
		elif uid != 0:
			response.update({'response':'user already exists'})
		else:
			response.update ({'response':'error: data'})
	else:
		response.update ({'response':'error: you may only perform a POST request'})
	return HttpResponse(simplejson.dumps(response), content_type='application/json')


@csrf_exempt
def update_or_return_list(request):
	response={}	
	print request.POST
	if request.POST['type'] == 'add':
		print "ADD"
		try:
			uid1 = request.POST['uid1']
			print "ADD1"
			uid2 = request.POST['uid2']
			print "ADD2"
			List.objects.create(uid1=uid1, uid2=uid2)
			print "ADD3"
			response.update({'response':'list updated'})
			print "ADD4"

		except BaseException:
			response.update({'response':'error'})
	elif request.POST['type'] == 'check':
		print "CHECK"
		try:
			uid = request.POST['uid']
			print "uid = " + uid

			if List.objects.filter(uid1=uid):
				a = List.objects.filter(uid1=uid).latest('create_time').uid1
			else:
				a = ''
			if List.objects.filter(uid2=uid):
				b = List.objects.filter(uid2=uid).latest('create_time').uid2
			else:
				b = ''
			if uid == a:
				response.update({'uid1':a})
			elif uid == b:
				response.update({'uid2':b})
			access_token = User.objects.get(id=uid).access_token
			facebook = select current_location, hometown_location, relationship_status, interests, education, work from user where uid = me()
			base_url = 'https://graph.facebook.com/fql?'
			r = requests.get((base_url + query_url))
			response.update({'response':r.json})
		except BaseException:
			response.update({'response':'error'})
	return HttpResponse(simplejson.dumps(response), content_type='application/json')


