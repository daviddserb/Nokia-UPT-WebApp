import os
import re
from webapp.models import TestLine, TestRun, TestCaseRun

def insert_db():
    folder_to_view = "webapp/logs"
    keywords = ["| PASS |", "| FAIL |"]
    keyword = [" -v CONFIGURATION"]

    for file_name in os.listdir(folder_to_view):
        print("# SE INTRA IN NOTEPAD #")
        # if file_name.endswith(".txt"): # extra, daca o sa am nevoie
        id_notepad = file_name.rpartition('.')[0] 
        print("id_notepad:")
        print(id_notepad)

        with open("webapp/logs/" + file_name, encoding="utf8") as fin:
            notepad_line_date = []
            notepad_line_name = []
            notepad_line_status = []
            for line in fin:
                if any(i in line for i in keyword):
                    notepad_config_id = line.split("UTESRANCLOUD")[1].strip()
                    print("notepad_config_id:")
                    print(notepad_config_id)

                if any(i in line for i in keywords):
                    notepad_line_date.append(re.search("\[(.*?)\,", line).group(1))
                    notepad_line_name.append(re.search("\] (.*?)\|", line).group(1))  # poate trebuie sa elimin spatiul alb
                    notepad_line_status.append(re.search("\| (.*?) \|", line).group(1))

        TestLine_insert = TestLine(
            id = notepad_config_id
            )
        TestLine_insert.save()

        TestRun_insert = TestRun(
            id = id_notepad,
            test_line = TestLine.objects.get(id = notepad_config_id)
            )
        TestRun_insert.save()

        for i in range(len(notepad_line_status)):
            TestCaseRun_insert = TestCaseRun(
                status = notepad_line_status[i],
                case_name = notepad_line_name[i],
                execution_time = notepad_line_date[i],
                test_run = TestRun.objects.get(id = id_notepad)
                )
            # INTREBARE: trebuie sa fac save() oare la fiecare save sau pot la finalul parcurgerii?
            TestCaseRun_insert.save()