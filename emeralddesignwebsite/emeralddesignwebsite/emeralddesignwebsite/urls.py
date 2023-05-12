from django.urls import path
from django.contrib import admin
from index.views import index, about, pricing
from contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('pricing/', pricing, name='pricing'),
    path('contact/', contact, name='contact'),
]
