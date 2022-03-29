from django.shortcuts import render
from django.http import HttpResponse

from webapp.models import TestLine, TestRun, TestCaseRun

def homepage(request):
    """
    register
    login
    ONLY VIEW configurations ids if user IS NOT logged in
    """
    return render(request, 'webapp/homepage.html')

def notepad_config_id(request):
    TestLine_data = TestLine.objects.all()
    return render(request, 'webapp/notepadConfigId.html', {'dataTestLine' : TestLine_data})

def id_notepad(request, notepad_config_id):
    TestRun_data = TestRun.objects.filter(test_line = notepad_config_id)
    return render(request, 'webapp/notepadIDs.html', {'dataTestRun' : TestRun_data, 'notepad_config_id' : notepad_config_id})

#! (cred) ordinea parametrilor NU conteaza, ci trebuie sa aiba aceleasi denumiri cu cele din path si daca trimiti 2 parametri prin path, trebuie sa se regaseasca amandoi aici
def notepad_details(request, notepad_config_id, notepad_id):
    #select the data from the table where each test_run has the id of the notepad
    print(notepad_config_id)
    print(notepad_id)
    TestCaseRun_data = TestCaseRun.objects.filter(test_run = notepad_id)
    return render(request, 'webapp/notepadDetails.html', {'dataTestCaseRun' : TestCaseRun_data})


# pt. testing
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)