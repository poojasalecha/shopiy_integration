from django.conf.urls import url

from . import views

""" urls """
urlpatterns = [
	url(r'^products/v1.0$', views.product_details, name='get_products'),
	url(r'^order/v1.0$', views.create_order, name='shopify_order'),
	

]