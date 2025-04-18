from django.urls import path
from . import views

# URL Config

urlpatterns = [
    path('hello/',views.sey_hello),
    path('test_templet/',views.test_templet)
]

