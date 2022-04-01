from django.db import models

# models.Model = clasa trebuie salvata in baza de date


class Users(models.Model):
    id = models.IntegerField(primary_key=True)  # contor
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    # test_line = models.ManyToManyField(TestLine) #cum fac aici?


class TestLine(models.Model):
    id = models.IntegerField(primary_key=True)  # id-ul din notepad, de dupa '-v REGISTER'


class TestRun(models.Model):
    id = models.IntegerField(primary_key=True)  # id-ul de la numele notepad-ului

    # ForeignKey = face legatura cu toata tabela, nu doar cu o anumita coloana
    # on_delete.CASCADE = cand clasa/obiectul, la care ForeignKey face referinta, este sters => se sterg si obiectele care au referinte la acesta (ex: cand stergi o pastare de blog, ar fi normal sa se stearga si comentariile de la acea postare)
    test_line = models.ForeignKey(TestLine, on_delete=models.CASCADE)


class TestCaseRun(models.Model):
    id = models.IntegerField(primary_key=True)  # contor
    status = models.CharField(max_length=10)
    case_name = models.CharField(max_length=200)
    execution_time = models.DateTimeField()
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE)
