from ..utils import Utils

""" transform data and return """
def transform(product):
	utils = Utils()
	print product, 'prrrr', type(product)
	return {
		'id': product.id,
		'title': product.title,
		'variants': utils.get_variants(product)
	}

	