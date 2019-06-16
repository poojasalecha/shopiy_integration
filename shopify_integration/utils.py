
""" python modules """
import uuid
import operator
from collections import defaultdict

""" local django """
from formatter.formatter import Formatter
from django.core.paginator import Paginator
from configuration.env import shopify_api_key, password
import shopify


""" Utility class """
class Utils(object):
	
	base_shopify_url = 'https://mishipayy.myshopify.com/admin/' 

	def get_shopify_client(self):
		shopify.ShopifyResource.set_user(shopify_api_key)
		shopify.ShopifyResource.set_password(password)
		shopify.ShopifyResource.set_site(self.base_shopify_url)
		return shopify

	def get_product_url(self):
		return self.base_shopify_url + '{0}'.format('api/2019-04/products.json') 

	def create_order_url(self):
		return "https://%s:%s@mishipayy.myshopify.com/admin/api/2019-04/orders.json" % (shopify_api_key, password)
	
	def get_items_and_page(self, reqeust):
		items = reqeust.GET.get('items')
		page = reqeust.GET.get('page')
		if not items:
			items = 10
		if not page:
			page = 1
		return items, page

	def get_variants(self, product):
		variants = []
		for variant in product.variants:
			variants.append({
				'inventoryItemId': variant.inventory_item_id,
				'inventoryQuantity': variant.inventory_quantity,
				'price': variant.price
			})
		return variants


	""" pagination
	@param reqeust, items
	@return paginated item
	 """
	def custom_pagination(self, request, items):
	    import math
	    page_number = 1 if not request.GET.get('page') else request.GET.get('page')
	    paginate_by =  1000 if not request.GET.get('item') else request.GET.get('item')
	    paginator = Paginator(items, paginate_by)
	    try:
	        page_number = int(page_number)
	    except:
	        page_number = 1
	    try:
	        items = paginator.page(page_number)
	    except:
	        items = paginator.page(1)

	    pagination  = {
	        'total_count': paginator.count,
	        'total_pages': int(math.ceil(float(paginator.count)/float(paginate_by))),        
	        'item': paginate_by,
	        'page': page_number
	    }
	    return items, pagination

