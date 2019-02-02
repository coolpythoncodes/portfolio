from django.urls import path

from .views import emailView, successView

urlpatterns = [
    path('contact/', emailView, name='contact'),
    path('success/', successView, name='success'),
]