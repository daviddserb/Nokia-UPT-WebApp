#DATABASE

from django.db import models

# from django.conf import settings #import the project settings into our models
# from django.utils import timezone #import this special timezone module to use date time objects

#models.Model = extending from the models object = is telling that this class needs to be saved into the database
class TestRun(models.Model):
    id = models.IntegerField(primary_key=True) #id-ul de la notepad_id.txt

    # daca vrei sa returnezi doar anumite coloane din tabel
    # def __str__(self):
        # return self.id
        
#print(TestRun.objects.all())

class TestCaseRun(models.Model):
    #If you don't explicitly define a primary key, then the table creates a default id which becomes your primary key
    id = models.IntegerField(primary_key=True) # INTEGER PRIMARY KEY is auto-incremented
    status =  models.CharField(max_length=10) #PASS | FAIL
    case_name = models.CharField(max_length=200)
    execution_time = models.DateTimeField()

    #on_delete.CASCADE = when the referenced object is deleted, also delete the object that have references to it (ex: when you remove a blog post, you might want to delete comments as well)
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE) #id-ul din TestRun

    def __str__(self):
        return self.status + self.case_name
        # nu pot returna si execution_time... pt ca ii de tip date?

#print(TestCaseRun.objects.all())