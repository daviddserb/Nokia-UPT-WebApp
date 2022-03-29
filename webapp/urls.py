from django.urls import path

from . import views

urlpatterns = [
    #pui ce path vrei
    path('', views.homepage, name='homepage'),
    path('config-id/', views.notepad_config_id, name='notepad_config_id'),
    path('config-id/<int:notepad_config_id>/', views.id_notepad, name='id_notepad'),
    #? Cum fac sa nu trebuiasca sa transmit notepad_config_id pt. ca nu am ce face cu el in fct din view
    path('config-id/<int:notepad_config_id>/<int:notepad_id>/', views.notepad_details, name='notepad_details'),

#pt. testing (de inteles)
    path('<int:question_id>/results/', views.results, name='results'),  # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/
]