from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsListView.as_view(), name='home'),
]
