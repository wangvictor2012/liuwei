from django.conf.urls import patterns, url

urlpatterns = patterns('paypal.standard.ipn.views',
                       url(r'^ipn/', 'ipn', name="paypalstd_ipn"),
                       url(r'^testbuy/', 'paypaltest_tpl_store_buy', name="paypalstd_test_buy"),
)
