from django.shortcuts import render, redirect
from django.contrib import messages #pop-up messages

from webapp.models import *
from .forms import *

def homepage(request):
    return render(request, 'webapp/homepage.html')

def register(request):
    print("### register ###")

    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST) # create a new form that has the data from the request.post (from the web form)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            print(username + ' ' + email + ' ' + password)

            Users_insert = Users(
                username = username,
                email = email,
                password = password,
                )
            Users_insert.save()

            messages.success(request, f'Account successfully created for the {username}!')
            #types of messages: .debug/info/success/warning/error

            return redirect('homepage')

    context = {'form':form}
    return render(request, 'webapp/register.html', context)

def login(request):
    print("### login ###")
    return render(request, 'webapp/login.html')

def notepad_config_id(request):
    TestLine_data = TestLine.objects.all()
    return render(request, 'webapp/notepadConfigId.html', {'dataTestLine' : TestLine_data})

def id_notepad(request, notepad_config_id):
    TestRun_data = TestRun.objects.filter(test_line = notepad_config_id)
    return render(request, 'webapp/notepadId.html', {'dataTestRun' : TestRun_data, 'notepad_config_id' : notepad_config_id})

#! (cred) ordinea parametrilor NU conteaza, ci trebuie sa aiba aceleasi denumiri cu cele din path si sa fie in acelasi numar
def notepad_details(request, notepad_config_id, notepad_id):
    #print(notepad_config_id)
    #print(notepad_id)
    TestCaseRun_data = TestCaseRun.objects.filter(test_run = notepad_id) #select the data from the table where each test_run has the id of the notepad
    return render(request, 'webapp/notepadDetails.html', {'dataTestCaseRun' : TestCaseRun_data})