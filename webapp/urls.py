from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),

    path('config-id/', views.Testline, name='Testline'),
    path('add-to-favorites/<int:notepad_config_id>/', views.add_favorites_TestLine, name="add_favorites_TestLine"),
    path('config-id/<int:notepad_config_id>/', views.Testrun, name='Testrun'),
    path('config-id/<int:notepad_config_id>/<int:notepad_id>/', views.Testcase, name='Testcase'),

    path('profile/', views.user_profile, name="userProfile"),
    path('favorites/', views.favorites_TestLine, name="favorites"),
    path('delete/<int:notepad_config_id>/', views.delete_favorites_TestLine, name="delete_favorites_TestLine"),
    path('logout/', views.logout_user, name='logout'),
]
