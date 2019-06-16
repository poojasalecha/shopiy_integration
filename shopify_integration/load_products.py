import shopify
import random
from configuration.env import shopify_api_key, password


def load_dummy_products():
	shop_url = "https://mishipayy.myshopify.com/admin"
	shopify.ShopifyResource.set_user(shopify_api_key)
	shopify.ShopifyResource.set_password(password)
	shopify.ShopifyResource.set_site(shop_url)

	dummy_products = [
		'shirt',
		'T-Shirt',
		'shoes',
		'belt',
		'watches',
		'trouser',
		'blanket'
	]

	for item in dummy_products:
		product = shopify.Product()
		product.title = item
		variant = shopify.Variant({'price': random.randint(100, 2500), 'inventory_item_id': random.randint(10000, 2500000), 'inventory_quantity': random.randint(100, 2500)})
		product.variants = [variant]
		product.save()
		print product.variants

if __name__ == '__main__':
	load_dummy_products()