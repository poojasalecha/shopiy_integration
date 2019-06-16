

def transform(order):
	""" order details """
	return {
		'id': order['id'],
		'createdAt': order['created_at'],
		'updatedAt': order['updated_at'],
		'totalPriceUsd': order['total_price_usd'],
		'lineItems': order['line_items']

	}