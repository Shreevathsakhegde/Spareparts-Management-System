"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from customer import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url('^logcheck', views.logcheck, name='logcheck'),

    url('^achangepassword', views.achangepassword, name='achangepassword'),
    url('^insertsparepartdetails', views.insertsparepartdetails, name='insertsparepartdetails'),
    url('^insertsupplier', views.insertsupplier, name='insertsupplier'),
    url('^insertCustomer', views.insertCustomer, name='insertCustomer'),
    url('^insertOrder', views.insertOrder, name='insertOrder'),
    url('^insertpayment', views.insertpayment, name='insertpayment'),
    url('^insertShipping', views.insertShipping, name='insertShipping'),
    url('^logcheck', views.logcheck, name='logcheck'),

url('^orderview', views.orderview, name='orderview'),
url('^paymentsview', views.paymentsview, name='paymentsview'),
url('^shippingview', views.shippingview, name='shippingview'),
url('^spare_partview', views.spare_partview, name='spare_partview'),
url('^supplierview', views.supplierview, name='supplierview'),
url('^customerview', views.customerview, name='customerview'),

url('^forgotpassword', views.forgotpassword, name='forgotpassword'),
url('newinsertOrder', views.newinsertOrder, name='newinsertOrder'),
url('^adminspare_partview', views.adminspare_partview, name='adminspare_partview'),

url('qrimg', views.qrimg, name='qrimg'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)