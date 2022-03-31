from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), # -> 3 options: register, login, config-id

    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),

    path('config-id/', views.notepad_config_id, name='notepad_config_id'),
    
    #path('config-id/<int:notepad_config_id>/', views.id_notepad, name='id_notepad'),
    path('config-id/<int:notepad_config_id>/', views.id_notepad, name='id_notepad'),

    #? Cum fac sa nu trebuiasca sa transmit notepad_config_id pt. ca nu am ce face cu el in fct din view
    #path('config-id/<int:notepad_config_id>/<int:notepad_id>/', views.notepad_details, name='notepad_details'),
    path('config-id/<int:notepad_config_id>/<int:notepad_id>/', views.notepad_details, name='notepad_details'),
]