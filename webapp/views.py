from django.shortcuts import render
from django.http import HttpResponse

from webapp.models import TestRun, TestCaseRun

def index(request):              

    #TestRun_data
    dataFromTableTestRun = TestRun.objects.all()
    return render(request, 'webapp/index.html', {'dataTestRun' : dataFromTableTestRun})

    #denumiri cu _: -> TestRun_details
def testRunDetails(request, notepad_id):
    """
    print(TestCaseRun.objects.all()) # MERGE 
    print(TestCaseRun.objects.values_list()) # MERGE
    print("---------")
    print(TestCaseRun.objects.filter(status = "FAIL")) # MERGE
    print(TestCaseRun.objects.filter(test_run = notepad_id)) # MERGE
    print("#########")
    """
    
    #select the data from the table where each test_run has the id of the notepad
    dataFromSelectedNotepad = TestCaseRun.objects.filter(test_run = notepad_id)
    return render(request, 'webapp/details.html', {'dataSelectedTable' : dataFromSelectedNotepad, 'notepadId' : notepad_id})


# pt. testing
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)