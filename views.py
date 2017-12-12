from django.shortcuts import render

import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect

from django.http import JsonResponse

def product_like(request, id):
	get_product = get_object_or_404(Product, id=id)
	rating_status = {}
	if request.is_ajax:
		if request.user in get_product.user.all():
			get_product.rating_count -= 1
			get_product.user.remove(request.user)
			get_product.save()
			rating_status['Removed'] = "True"
			rating_status['count'] = get_product.rating_count
			return HttpResponse(JsonResponse(rating_status))
		else:
			get_product.rating_count += 1
			get_product.user.add(request.user)
			get_product.save()
			rating_status['Success'] =  "True"
			rating_status['count'] = get_product.rating_count
			return HttpResponse(JsonResponse(rating_status))
	else:
		rating_status['Success'] =  "False"
		return HttpResponse(JsonResponse(rating_status))
	return request