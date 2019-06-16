
""" local imports """
from .utils import Utils
from .basecontroller import BaseController
from transformer import ProductTransformer, OrderTransformer
from formatter.formatter import Formatter

""" djanngo imports """
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import requests
import json, re
import httplib

# Create your views here.



@csrf_exempt
def product_details(request):

	""" prodcuct list
	@return product details
	 """
	if request.method == 'GET':
		try:
			result = []
			utils = Utils()
			items , page = utils.get_items_and_page(request)
			shopify = utils.get_shopify_client()
			products = shopify.Product.find(item =items, page=page)
			return BaseController().respond_with_paginated_collection(httplib.OK, products, ProductTransformer, page, items)
		except Exception:
			return BaseController().respond_with_error(httplib.INTERNAL_SERVER_ERROR, 'something went wrong')
	return BaseController().respond_with_error(httplib.METHOD_NOT_ALLOWED, 'please check your method')

@csrf_exempt
def create_order(request):


	""" create order in shopify
	@return order details
	"""
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			utils = Utils()
			formatter = Formatter()
			create_order_url = utils.create_order_url()
			order_data = formatter.get_order_data(data)
			response = requests.post(create_order_url, json=order_data)
			if response.status_code == httplib.CREATED:
				response = json.loads(response.content)
				return BaseController().respond_with_item(httplib.OK, response['order'], OrderTransformer)
			return BaseController().respond_with_error(httplib.INTERNAL_SERVER_ERROR, 'order not created')
		except Exception:
			return BaseController().respond_with_error(httplib.INTERNAL_SERVER_ERROR, 'something went wrong')
	return BaseController().respond_with_error(httplib.METHOD_NOT_ALLOWED, 'please check your method')










