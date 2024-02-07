from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # Authentication
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # User management
    path('list/', views.users_list, name="list")
]
