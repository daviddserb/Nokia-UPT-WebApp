from django.db import models
from django.contrib.auth.models import User  # db.sqlite3/auth_user


# models.Model = clasa trebuie salvata in baza de date
class TestLine(models.Model):
    id = models.IntegerField(primary_key=True)  # id-ul '-v REGISTER'
    users = models.ManyToManyField(User)


class TestRun(models.Model):
    id = models.IntegerField(primary_key=True)  # notepad id

    """
    ForeignKey = face legatura cu toata tabela, nu doar cu o anumita coloana

    on_delete.CASCADE = cand clasa la care FK face referinta este stearsa
    => se sterg si obiectele care au referinte la acesta
    (cand stergi o pastare, este normal sa se stearga si comentariile)
    """
    test_line = models.ForeignKey(TestLine, on_delete=models.CASCADE)


class TestCase(models.Model):
    id = models.IntegerField(primary_key=True)  # contor
    status = models.CharField(max_length=10)
    case_name = models.CharField(max_length=200)
    execution_time = models.DateTimeField()
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE)
