from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),

    path('config-id/', views.notepad_config_id, name='notepad_config_id'),
    # can add-to-favorites only if logged in
    path('add-to-favorites/<int:notepad_config_id>/', views.add_to_favorites, name="add_to_favorites"),
    path('config-id/<int:notepad_config_id>/', views.id_notepad, name='id_notepad'),
    path('config-id/<int:notepad_config_id>/<int:notepad_id>/', views.notepad_details, name='notepad_details'),

    # if the user is logged in => show his profile
    path('profile/', views.user_profile, name="userProfile"),

    path('favorites/', views.favorites, name="favorites"),
    path('delete/<int:notepad_config_id>/', views.deleteId, name="deleteId"),

    path('logout/', views.logout_user, name='logout'),
]