from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import random
import string
import json
from django.core.files.storage import FileSystemStorage
import pika

# Create your views here.
class FilesMethods(object):
	@csrf_exempt
	def render(request):
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["password"]
			allUrl = []
			urlFile1 = request.POST["urlFile1"]
			urlFile2 = request.POST["urlFile2"]
			urlFile3 = request.POST["urlFile3"]
			urlFile4 = request.POST["urlFile4"]
			urlFile5 = request.POST["urlFile5"]
			urlFile6 = request.POST["urlFile6"]
			urlFile7 = request.POST["urlFile7"]
			urlFile8 = request.POST["urlFile8"]
			urlFile9 = request.POST["urlFile9"]
			urlFile10 = request.POST["urlFile10"]
			allUrl.append(urlFile1)
			allUrl.append(urlFile2)
			allUrl.append(urlFile3)
			allUrl.append(urlFile4)
			allUrl.append(urlFile5)
			allUrl.append(urlFile6)
			allUrl.append(urlFile7)
			allUrl.append(urlFile8)
			allUrl.append(urlFile9)
			allUrl.append(urlFile10)
			credentials = pika.PlainCredentials('1506725003', '697670')
			connection = pika.BlockingConnection(pika.ConnectionParameters('152.118.148.103',5672,'1506725003', credentials))
			channel = connection.channel()
			exchange = '1506725003'
			channel.exchange_declare(exchange=exchange, exchange_type='direct', passive=False, durable=False, auto_delete=False)
			url = "https://oauth.infralabs.cs.ui.ac.id/oauth/token"
			data = {"username": username, "password": password, "grant_type": "password", "client_id": "nCpJE0ZFYp7YMlyVok0ughAPQgFlfk2w", "client_secret": "J7QOAJ1To5Rjt4S7tOeBwKNyY0Eb6RLI"}
			r = requests.post(url, data = data)
			if r.status_code == 401 :
				return JsonResponse({"status" : "error", "description": "Unauthorized wrong username or password"}, status=401)
			else :
				json_data = r.json()
				# request.session['username'] = username
				token = json_data['access_token']
			if(urlFile1 != "" and urlFile2 != "" and urlFile3 != "" and urlFile4 != "" and urlFile5 != "" and urlFile6 != "" and urlFile7 != "" and urlFile8 != "" and urlFile9 != "" and urlFile10 != ""):
			# if(urlFile1 != "" and urlFile2 != "" and urlFile3 != ""):
				counter = 1
				for url in allUrl:
					data = str(counter) + ";" + url + ";" + token
					counter += 1
					print(data)
					channel.basic_publish(exchange=exchange,
						routing_key='dataServer1',
						body=data)
			else:
				return JsonResponse({"status" : "error", "description": "Filled all the url"}, status=401)
			# uniqueId = FilesMethods.randomString(16)
			# urlServer = "http://1506725003.law.infralabs.cs.ui.ac.id:20218/upload"
			# fs = FileSystemStorage()
			# filename = fs.save(newFile.name, newFile)
			# uploadedFilePath = fs.path(filename)

			# files = {'uploadedFile':(newFile.name, newFile)}
			# header = {'X-ROUTING-KEY': uniqueId}
			# allData = username + ";" + password + ";" + filename + ";" + uniqueId
			# credentials = pika.PlainCredentials('1506725003', '697670')
			# connection = pika.BlockingConnection(pika.ConnectionParameters('152.118.148.103',5672,'1506725003', credentials))
			# channel = connection.channel()
			# exchange = '1506725003'
			# channel.exchange_declare(exchange=exchange, exchange_type='direct', passive=False, durable=False, auto_delete=False)
			# channel.basic_publish(exchange=exchange,
			# 	routing_key='dataServer1',
			# 	body=allData)
			# connection.close()
			# while(True) :
			# 	ts = datetime.datetime.today().strftime('%A, %d %B %Y, %H:%M:%S')
			# 	print(ts)
			# 	channel.basic_publish(exchange=exchange,
			# 						  routing_key='waktuServer',
			# 						  body=ts)
			# 	time.sleep(1)
			# connection.close()
			# return JsonResponse({"status": "ok"})
			return render(request, 'files/index.html', {})

			# try:
			# 	r = requests.post(urlServer, files=files, headers=header)
			# 	if r.status_code == 200:
			# 		return render(request, 'files/index.html', {'uniqueId': uniqueId})
			# 	else:
			# 		return render(request, 'files/index.html', {'error': "Internal server error"})
			# except requests.exceptions.ConnectionError:
			# 	return render(request, 'files/index.html', {'error': 'Connection Error check your backend service'})
		else:
			return render(request, 'files/index.html', {})