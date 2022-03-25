from django.urls import path

from . import views

# nu stiu daca am nevoie de asta
# app_name = 'webapp' # webapp -> templates -> webapp

urlpatterns = [
    # pot sa pui ce path vrei la ''
    path('', views.index, name='index'),

    #pt. testing (de inteles)
    path('<int:question_id>/', views.detail, name='detail'), # ex: /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),  # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/
]