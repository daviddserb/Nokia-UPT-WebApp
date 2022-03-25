#views = logic / algorithms

from django.shortcuts import render
from django.http import HttpResponse

import os, re, sqlite3
from webapp.models import TestRun, TestCaseRun

def index(request):
    print("def index(request)")
    folder_to_view = "webapp/logs"
    keywords = ["| PASS |", "| FAIL |"]
    
    for file_name in os.listdir(folder_to_view):
        if file_name.endswith(".txt"):
            print(file_name)
            print(file_name.rpartition('.'))
            id_notepad = file_name.rpartition('.')[0] #pt. baza de date
            print(id_notepad)

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

    print("#########################")
    print(TestCaseRun.objects.all())
    print("-------------------------")
    print(TestRun.objects.all())
    print(TestRun.objects.all().values_list())
    print(TestRun.objects.all()[0])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    #print(TestCaseRun.id)
    #print(TestCaseRun.id)
    #print(TestCaseRun.case_name)

    dataTestRun = TestRun.objects.all()
    # data from DB
    # context = {TestRun.objects.get}
    # print("context:")
    # print(context)
    return render(request, 'webapp/index.html', {'idTestRun' : dataTestRun})

#pt. testing
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)