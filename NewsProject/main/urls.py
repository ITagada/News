from django.urls import path
from .views import index, get_profession, view_human, add_human

urlpatterns = [
    path('', index, name='home'),
    path('profession/<int:profession_id>', get_profession, name='profession'),
    path('human/<int:human_id>', view_human, name='view_human'),
    path('human/add_human', add_human, name='add_human')
]
