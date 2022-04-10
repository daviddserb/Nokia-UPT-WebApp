from django.shortcuts import render, redirect
from django.contrib import messages  # pop-up messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # db.sqlite3/quth_user

from webapp.models import TestLine, TestRun, TestCaseRun
from .forms import RegisterUserForm

def home(request):
    return render(request, 'webapp/home.html')

def register(request):
    # form = RegisterUserForm(None or request.POST)
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST) # create a new form that has the data from the html form post request
        
        # verifica daca fiecare camp din form este valid, pentru clasa Django Form. Daca datele sunt valide, se salveaza in atributul cleaned_data
        if form.is_valid():
            # save user in the django database (auth_user)
            form.save()

            # get user input from the html form
            username = form.cleaned_data['username']

            # pop-up message
            messages.success(request, f"Account successfully created for '{username}'!")
            # types of messages: .debug/info/success/warning/error

            return redirect('login_user')

    context = {'form' : form}
    return render(request, 'webapp/register.html', context)

def login_user(request):
    if request.method == 'POST':
        
        # get data from html
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        # check if the user is in the database
        if user is not None:
            login(request, user)
            return redirect('/webapp/profile')
        else:
            messages.warning(request, "This account is not registered!")

    return render(request, 'webapp/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def user_profile(request):
    print("! user_profile !")
    context = {'userInfo' : request.user}
    return render(request, 'webapp/userProfile.html', context)

def favorites(request):
    print("@ favorites @")
    favorites_id = TestLine.objects.filter(users = request.user)
    print("toate id-urile adaugate la favorite de user-ul logat")
    print(favorites_id)

    context = {'favs_id' : favorites_id}
    return render(request, 'webapp/favorites.html', context)

def deleteId(request, notepad_config_id):
    print(" @ deleteId @")
    """
    many to many field instance: NameTableWithManyToManyField.NameReferencedTable
    intermediary table model: NameTableWithManyToManyField.NameReferencedTable.through
    intermediary model manager: NameTableWithManyToManyField.NameReferencedTable.through.objects
    return a queryset for all intermediary models: NameTableWithManyToManyField.NameReferencedTable.through.objects.all()
    """

    select = TestLine.users.through.objects.filter(testline_id = notepad_config_id, user_id = request.user.id)
    select.delete()
    
    return redirect('favorites')


def notepad_config_id(request):
    print("request.user:")
    print(request.user)
    TestLine_data = TestLine.objects.all()
    context = {'dataTestLine' : TestLine_data, 'userName' : str(request.user)}
    return render(request, 'webapp/notepadConfigId.html', context)

def add_to_favorites(request, notepad_config_id):
    print("# add_to_favorites #")

    # INTREBARE: aparent merge dar nu-mi dau seama exact unde se intampla fiecare bucata din logica.
    testline = TestLine.objects.get(id = notepad_config_id)
    # filter() - returns a QuerySet even if only one object is found.
    # get() - returns just one single model instance.
    print("id-ul care a fost adaugat la favorite de catre user-ul logat:")
    print(testline)

    testline.users.add(request.user)
    # INTREBARE: nu-mi dau seama ce face save(), cu/fara tot aia e.
    # testline.save()

    print("toti userii care au adaugat la favorite id-ul respectiv:")
    print(testline.users.all())

    return redirect('favorites')


def id_notepad(request, notepad_config_id):
    TestRun_data = TestRun.objects.filter(test_line = notepad_config_id)
    return render(request, 'webapp/notepadId.html', {'dataTestRun' : TestRun_data, 'notepad_config_id' : notepad_config_id})

# ordinea parametrilor nu conteaza, ci trebuie sa aiba aceleasi denumiri cu cele din path si sa fie in acelasi numar
def notepad_details(request, notepad_config_id, notepad_id):
    print("notepad_config_id:")
    print(notepad_config_id)
    print("notepad_id:")
    print(notepad_id)
    TestCaseRun_data = TestCaseRun.objects.filter(test_run = notepad_id)  # select the data from the table where each test_run has the id of the notepad
    return render(request, 'webapp/notepadDetails.html', {'dataTestCaseRun' : TestCaseRun_data})