from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsListView.as_view(), name='home'),
    path('remove/<int:pk>', views.JobsDeleteView.as_view(),  name='remove'),
]
