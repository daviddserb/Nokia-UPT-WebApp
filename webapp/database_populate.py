import os, re
from webapp.models import TestRun, TestCaseRun

def populate_database():
    folder_to_view = "webapp/logs"
    keywords = ["| PASS |", "| FAIL |"]

    for file_name in os.listdir(folder_to_view):
            # if file_name.endswith(".txt"):
            #print(file_name)
            id_notepad = file_name.rpartition('.')[0]
            #print(id_notepad)

            #? asta cred ca nu se mai salveaza repetat in baza de date pt. ca id ii PK
            insertInTable_TestRun = TestRun(
                id = id_notepad
                )
            insertInTable_TestRun.save()

            with open("webapp/logs/" + file_name, encoding="utf8") as fin:
                for line in fin:
                    if any(i in line for i in keywords):
                        
                        print(line) #(pt. a evita la printare \n pot pune: line.strip()

                        line_date = re.search("\[(.*?)\,", line)
                        print(line_date.group(1))
                        

                        lineName = re.search("\] (.*?)\|", line)
                        print(lineName.group(1))

                        lineStatus = re.search("\| (.*?) \|", line)
                        print(lineStatus.group(1))

                        
                        insertInTable_TestCaseRun = TestCaseRun(
                            status = lineStatus.group(1),
                            case_name = lineName.group(1),
                            execution_time = line_date.group(1),
                            test_run = TestRun.objects.get(id = id_notepad)
                            )
                        insertInTable_TestCaseRun.save()