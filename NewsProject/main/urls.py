from django.urls import path
from .views import HomeHuman, HumanProfession, ViewHuman, AddHuman, register, user_login, user_logout

# from .views import index, get_profession, view_human, add_human

urlpatterns = [
    # path('', index, name='home'),
    # path('profession/<int:profession_id>', get_profession, name='profession'),
    # path('human/<int:human_id>', view_human, name='view_human'),
    # path('human/add_human', add_human, name='add_human'),
    path('', HomeHuman.as_view(), name='home'),
    path('profession/<int:pk>', HumanProfession.as_view(), name='profession'),
    path('human/<int:pk>', ViewHuman.as_view(), name='view_human'),
    path('human/add_human', AddHuman.as_view(), name='add_human'),
    path('register', register, name='Register'),
    path('login', user_login, name='Login'),
    path('logout', user_logout, name='Logout'),
]
