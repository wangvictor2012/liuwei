from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:

    # Include the URLs for the website
    url(r'^paypalstd/', include('paypal.standard.ipn.urls'), name='paypalstd_ipn'),
	#url(r'paypalpdt/', include('paypal.standard.pdt.urls'), name='paypalstd_pdt'),
)
