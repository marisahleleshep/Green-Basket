from django.urls import path
from .views import payment_upload


urlpatterns = [
    
    path('payment/upload/', payment_upload, name='payment_upload_view'),

]