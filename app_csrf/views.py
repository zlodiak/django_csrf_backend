from django.http import HttpResponse
from django.middleware.csrf import rotate_token
from django.views.decorators.csrf import csrf_exempt
import random


def display_form(request):
	response = HttpResponse('set csrf cookie for form')
	# ещё один способ сгенерировать токен и сразу поместить его в соответствующий заголовок, но уже средствами фреймворка
	# rotate_token(request)  
	response.set_cookie('csrftoken', random.getrandbits(256))
	response['Access-Control-Allow-Origin'] = 'http://localhost:4200'
	response['Access-Control-Allow-Credentials'] = 'true'
	return response	


@csrf_exempt
def transfer_money(request):
	print(); print(); print(); print(); print(); print(); print()
	print('__________________________________________________________________________REQUEST METHOD: ' + request.method)
	print(); print(); print()

	if request.method == 'OPTIONS':
		print('----------------condition block for OPTIONS is activate')
		response = HttpResponse('money transfer preflight')	
		print(); print(); print()
		
		response['Access-Control-Allow-Origin'] = 'http://localhost:4200'		
		response['Access-Control-Allow-Headers'] = 'X-XSRF-TOKEN, Content-Type'		

		return response

	if request.method == 'POST':
		print('----------------condition block for  POST is activate')
		print('recieved form data:')
		for x in request: print(x)
		print(); print(); print()
		
		# if comparison_cookies_procedure():
		# 	print('operation is successful')
		# else:
		# 	print('operation is failed')

		response = HttpResponse('status: operation is __RESULT__')	
		return response