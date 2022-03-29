from django.db import models

#models.Model = is telling that this class needs to be saved into the database

class TestLine(models.Model):
    id = models.IntegerField(primary_key=True) #id-ul din notepad, de dupa '-v REGISTER'

class TestRun(models.Model):
    id = models.IntegerField(primary_key=True) #id-ul de la numele notepad-ului
    test_line = models.ForeignKey(TestLine, on_delete=models.CASCADE)

class TestCaseRun(models.Model):
    id = models.IntegerField(primary_key=True) #id de contorizare
    status =  models.CharField(max_length=10)
    case_name = models.CharField(max_length=200)
    execution_time = models.DateTimeField()

    #on_delete.CASCADE = when the referenced object is deleted, also delete the objects that have references to it (ex: when you remove a blog post, you might want to delete comments as well)
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE)