from django.urls import path
from .views import shipping_upload


urlpatterns = [
    
    path('shipping/upload/', shipping_upload, name='shipping_upload_view'),

]