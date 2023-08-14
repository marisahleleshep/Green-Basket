from django.urls import path
from . import views


urlpatterns = [
    path('feedback/upload/', views.upload_feedback, name='upload_feedback'),
    path('feedback/upload-feedbacks/', views.upload_feedbacks, name='upload_feedbacks'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
    path('feedback/detail/<int:id>/', views.feedback_details, name='feedback_detail_view'),
    path('feedback/edit/<int:id>/', views.edit_feedback_view, name='edit_feedback_view'),
]
