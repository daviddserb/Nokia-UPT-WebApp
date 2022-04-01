from django.shortcuts import render, redirect
from django.contrib import messages  # pop-up messages
from django.contrib.auth import authenticate, login, logout

from webapp.models import Users, TestLine, TestRun, TestCaseRun
from .forms import *

def homepage(request):
    return render(request, 'webapp/homepage.html')

def register(request):

    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST) # create a new form that has the data from the request.post (from the web form)
        
        # verifica daca fiecare camp din form este valid, pentru clasa Django Form. Daca datele sunt valide, se salveaza in atributul cleaned_data
        if form.is_valid():
            """INTREBARE:
            nu am prea inteles ce face
            nu imi afecteaza salvara in baza de date
            dar am vazut ca pe ruta de /admin, la Useri, nu vad cel care s-a inregistrat, daca nu am form.save()"""
            form.save()

            #get data from the html
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            #save in database like this (I have to try)
            # register = Users.objects.create(username=username, email=email, password=password)
            # trebuie cumva sa il si salvez...?
            # register.save() #(cred)

            #save data in database
            Users_insert = Users(
                username = username,
                email = email,
                password = password,
                )
            Users_insert.save()

            messages.success(request, f"Account successfully created for '{username}'!")
            #types of messages: .debug/info/success/warning/error

            return redirect('homepage')

    context = {'form':form}
    return render(request, 'webapp/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        
        #get data from html
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        #check if the user is in the database
        if user is not None:
            login(request, user)
            return redirect('/webapp/profile')
        else:
            messages.warning(request, "This account is not registered!")

    return render(request, 'webapp/login.html')

def userProfile(request):
    print("############### userProfile()                       #######################")
    return render(request, 'webapp/userProfile.html')

def notepad_config_id(request):
    print("############################### SE INTRA IN NOTEPAD_CONFIG_ID")
    TestLine_data = TestLine.objects.all()
    return render(request, 'webapp/notepadConfigId.html', {'dataTestLine' : TestLine_data})

def id_notepad(request, notepad_config_id):
    TestRun_data = TestRun.objects.filter(test_line = notepad_config_id)
    return render(request, 'webapp/notepadId.html', {'dataTestRun' : TestRun_data, 'notepad_config_id' : notepad_config_id})

#! (cred) ordinea parametrilor NU conteaza, ci trebuie sa aiba aceleasi denumiri cu cele din path si sa fie in acelasi numar
# def notepad_details(request, notepad_config_id, notepad_id):
def notepad_details(request, notepad_config_id, notepad_id):
    #print(notepad_config_id)
    #print(notepad_id)
    TestCaseRun_data = TestCaseRun.objects.filter(test_run = notepad_id) #select the data from the table where each test_run has the id of the notepad
    return render(request, 'webapp/notepadDetails.html', {'dataTestCaseRun' : TestCaseRun_data})