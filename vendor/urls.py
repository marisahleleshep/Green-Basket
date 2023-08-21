from django.urls import path
from .views import upload_vendor_registrations


urlpatterns = [
    
    path('vendor/upload/', upload_vendor_registrations, name='vendor_upload_view'),

]