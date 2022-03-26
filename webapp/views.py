#views = logic / algorithms

from django.shortcuts import render
from django.http import HttpResponse

import os, re, sqlite3
from webapp.models import TestRun, TestCaseRun

def index(request):
    folder_to_view = "webapp/logs"
    keywords = ["| PASS |", "| FAIL |"]
    
    for file_name in os.listdir(folder_to_view):
        if file_name.endswith(".txt"):
            # print(file_name)
            id_notepad = file_name.rpartition('.')[0] #pt. baza de date
            # print(id_notepad)

            insertInTable_TestRun = TestRun(
                id = id_notepad
                )
            insertInTable_TestRun.save()

            with open("webapp/logs/" + file_name, encoding="utf8") as fin:
                for line in fin:
                    if any(i in line for i in keywords):
                        #print(line) #(pt. a evita la printare \n pot pune: line.strip()

                        lineDate = re.search("\[(.*?)\,", line)
                        #print(lineDate.group(1))
                        

                        lineName = re.search("\] (.*?)\|", line)
                        #print(lineName.group(1))

                        lineStatus = re.search("\| (.*?) \|", line)
                        #print(lineStatus.group(1))

                        """
                        insertInTable_TestCaseRun = TestCaseRun(
                            status = lineStatus.group(1),
                            case_name = lineName.group(1),
                            execution_time = lineDate.group(1),
                            test_run = TestRun.objects.get(id = id_notepad)
                            )
                        insertInTable_TestCaseRun.save()
                        """

    dataFromTableTestRun = TestRun.objects.all()
    return render(request, 'webapp/index.html', {'dataTestRun' : dataFromTableTestRun})

def testRunDetails(request, notepad_id):
    dataFromTableTestCaseRun = TestCaseRun.objects.all()
    return render(request, 'webapp/details.html', {'dataTestCaseRun' : dataFromTableTestCaseRun})


# pt. testing
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)