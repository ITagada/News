from django.urls import path
from .views import index, get_profession

urlpatterns = [
    path('', index, name='home'),
    path('profession/<int:profession_id>', get_profession, name='profession')
]
