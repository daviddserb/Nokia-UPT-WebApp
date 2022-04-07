from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.login_user, name='login_user'),
    path('profile/', views.userProfile, name="userProfile"),

    path('config-id/', views.notepad_config_id, name='notepad_config_id'),

    #path('config-id/<int:notepad_config_id>/', views.id_notepad, name='id_notepad'),
    # INTREBARE:
    # aici daca scot config-id dispare de pe ruta. pot cumva sa il scot de aici din path dar sa ramana totusi pe ruta?
    path('config-id/<int:notepad_config_id>/', views.id_notepad, name='id_notepad'),
    
    # ??? INTREBARE:
    # la fel si aici, ce am zis mai sus, sa ramana ambele.
    #path('config-id/<int:notepad_config_id>/<int:notepad_id>/', views.notepad_details, name='notepad_details'),
    path('config-id/<int:notepad_config_id>/<int:notepad_id>/', views.notepad_details, name='notepad_details'),
]