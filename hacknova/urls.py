from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="Admin Panel"),
    path('api/', include('apis.urls')),
    path('whatsapp/', include('whatsapp.urls')),
    path('payment/', include('payment.urls')),
    path('onlinemeet/', include('online.urls')),
]
