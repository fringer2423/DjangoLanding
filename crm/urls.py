from django.urls import path
from .views import index, thanks

urlpatterns = [
    path('', index, name='index'),
    path('thanks/', thanks, name='thanks')
]
