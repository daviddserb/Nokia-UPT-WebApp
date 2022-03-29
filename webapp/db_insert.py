import os
import re

from webapp.models import TestLine, TestRun, TestCaseRun

def insert_db():
    folder_to_view = "webapp/logs"
    keywords = ["| PASS |", "| FAIL |"]
    keyword = [" -v CONFIGURATION"]

    for file_name in os.listdir(folder_to_view):
            # if file_name.endswith(".txt"): (extra, daca o sa am nevoie)
            #print(file_name)
            notepad_id = file_name.rpartition('.')[0]
            #print(notepad_id)

            with open("webapp/logs/" + file_name, encoding="utf8") as fin:
                for line in fin:
                    if any(i in line for i in keywords):
                        #print(line) #(pt. a evita la printare \n pot pune: line.strip()

                        line_date = re.search("\[(.*?)\,", line)
                        #print(line_date.group(1))
                        
                        line_name = re.search("\] (.*?)\|", line)
                        #print(line_name.group(1))

                        line_status = re.search("\| (.*?) \|", line)
                        #print(line_status.group(1))

                        TestCaseRun_insert = TestCaseRun(
                            status = line_status.group(1),
                            case_name = line_name.group(1),
                            execution_time = line_date.group(1),
                            test_run = TestRun.objects.get(id = notepad_id)
                            )
                        TestCaseRun_insert.save()

                    if any(i in line for i in keyword):
                        line_id = line.split("UTESRANCLOUD")[1].strip()

                        TestLine_insert = TestLine(
                            id = line_id
                            )
                        TestLine_insert.save()

                        TestRun_insert = TestRun(
                            id = notepad_id,
                            test_line = TestLine.objects.get(id = line_id)
                            )
                        TestRun_insert.save()