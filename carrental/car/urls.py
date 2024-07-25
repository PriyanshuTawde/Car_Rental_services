from django.urls import path
from .views import Contact_Us

urlpatterns = [
    path('create/contactus', Contact_Us ,name="contactus"),
]
