from django.urls import path
from .views import account_registrations_list,upload_account_registrations,account_registrations_details,edit_account_registrations_view

urlpatterns = [
    path('account_registration/list/', account_registrations_list, name='account_registration_list'),

    path('account_registration/upload/', upload_account_registrations, name='upload_account_registrations'),
    # path('account_registration/list', account_registrations_list, name='account_list_view'),
    path('account_registration/detail/<int:id>/', account_registrations_details, name='account_registration_detail_view'),
    path('account_registration/edit/<int:id>/', edit_account_registrations_view, name='edit_account_registration_view'),
]
