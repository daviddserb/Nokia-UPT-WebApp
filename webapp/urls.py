from django.urls import path

from . import views

urlpatterns = [
    # pot sa pui ce path vrei
    #path simplu pt webapp
    path('logs', views.index, name='index'),
    path('logs/<int:notepad_id>', views.testRunDetails, name='testRunDetails'),

#pt. testing (de inteles)
    path('<int:question_id>/results/', views.results, name='results'),  # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/
]