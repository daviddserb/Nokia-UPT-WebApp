from django.shortcuts import render, redirect
from django.contrib import messages  # pop-up messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # db.sqlite3/auth_user
from webapp.models import TestLine, TestRun, TestCase
from .forms import RegisterUserForm


def home(request):
    total_accounts = User.objects.count()

    context = {'accounts': total_accounts}
    return render(request, 'webapp/home.html', context)


def register(request):
    # form = RegisterUserForm(None or request.POST)
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        # verifica daca fiecare camp din form este valid pt. clasa Django Form.
        # daca datele sunt valide, se salveaza in atributul cleaned_data.
        if form.is_valid():
            # save user in the django database (auth_user)
            form.save()

            # get user input from the html form
            username = form.cleaned_data['username']

            # pop-up message
            messages.success(request, f"Account successfully created for '{username}'!")
            # types of messages: .debug/info/success/warning/error

            return redirect('login_user')

    context = {'form': form}
    return render(request, 'webapp/register.html', context)


def login_user(request):
    if request.method == 'POST':

        # get data from html
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

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
    # request.user prints only the name, BUT it's not the same as request.user.username, because that's what it only wants to print, but inside it's actually all the information from db
    total_Testcases = TestCase.objects.count()

    context = {'userInfo': request.user, 'testcases': total_Testcases}
    return render(request, 'webapp/userProfile.html', context)


def favorites_TestLine(request):
    favorites_id = TestLine.objects.filter(users=request.user)

    print("toate 'id-urile' adaugate la favorite de user-ul logat:")
    print(favorites_id)

    context = {'favs_id': favorites_id}
    return render(request, 'webapp/favoritesTestLine.html', context)


def delete_favorites_TestLine(request, notepad_config_id):
    # testline = TestLine.objects.all().delete() -> to delete all TestLines (and will delete also TestRun and TestCase because of the cascade)

    testline = TestLine.objects.filter(id=notepad_config_id).first()
    testline.users.remove(request.user)

    return redirect('favorites')


def Testline(request):
    TestLine_data = TestLine.objects.all()

    context = {'dataTestLine': TestLine_data, 'userName': str(request.user)}
    return render(request, 'webapp/TestLine.html', context)


def add_favorites_TestLine(request, notepad_config_id):
    # filter() - returns a QuerySet even if only one object is found.
    # get() - returns just one single model instance.
    testline = TestLine.objects.get(id=notepad_config_id)

    print("'id-ul' care a fost adaugat la favorite de catre user-ul logat:")
    print(testline)

    testline.users.add(request.user)

    print("toti userii care au adaugat la favorite 'id-ul' respectiv:")
    print(testline.users.all())

    return redirect('favorites')


def Testrun(request, notepad_config_id):
    # when the user tries manually to put a number in the path of the page
    if not TestLine.objects.filter(id=notepad_config_id).exists():
        return render(request, 'webapp/404.html')

    Testruns = TestRun.objects.filter(test_line=notepad_config_id)
    print("'id-urile' notepad-urilor care au acelasi 'id' in interiorul lor")
    print(Testruns)

    passed = []
    failed = []
    for Testrun in Testruns:
        TestCase_lines = TestCase.objects.filter(test_run_id=Testrun.id)  # toate 'liniile de teste' (nume, status, data) care apartin notepad-ului click-uit

        total_tests = TestCase_lines.count()
        print("TOTAL:")
        print(TestCase_lines.count())

        passed_tests = TestCase_lines.filter(status='PASS').count()
        print("PASS:")
        print(TestCase_lines.filter(status='PASS').count())

        failed_tests = TestCase_lines.filter(status='FAIL').count()
        print("FAIL:")
        print(TestCase_lines.filter(status='FAIL').count())

        passed.append(format((passed_tests / total_tests) * 100, ".2f"))
        failed.append(format((failed_tests / total_tests) * 100, ".2f"))

    Testrunes_Testcases = zip(Testruns, passed, failed)
    
    isFavorite = "NO"
    if(str(request.user) != "AnonymousUser"):
        # go through the entire many-to-many table and search if the logged in user added that testline to the favorites
        TestLine_users = TestLine.users.through.objects.filter(testline_id=notepad_config_id, user_id=request.user)
        print(TestLine_users)

        """
        difference between .filter(A, B) VS filter(A).filter(B):

        - to extract all blogs from 2008 AND who have "Lennon" as title: .filter(title='Lennon', year=2008).
        - to extract all blogs from 2008 OR who have "Lennon" as title: .filter(title='Lennon').filter(year=2008).
        
        - so .filter(A, B) will first filter EVERYTHING according to A and then subfilter (filter again the RESULT) according to B.
        - while .filter(A).filter(B) will filter EVERYTHING according to A and have a result, and then filter again EVERYTHING and have another result, which may not corespond to the A condition.
        """

        # check if QuerySet is empty. If it is => the logged in user DID NOT add that testline to his favorites
        if TestLine_users:
            isFavorite = "YES"

    context = {'Testcases_details': Testrunes_Testcases, 'notepad_config_id': notepad_config_id, 'userName': str(request.user), 'isFavorite': isFavorite}
    return render(request, 'webapp/TestRun.html', context)


# ordinea parametrilor nu conteaza, trebuie sa aiba aceleasi denumiri cu cele din path si sa fie in acelasi numar
def Testcase(request, notepad_config_id, notepad_id):
    # when the user tries manually to put a random number in the path of the page
    if not TestRun.objects.filter(id=notepad_id).exists():
        return render(request, 'webapp/404.html')

    # select data from table where each TestCase has the id of TestRun
    TestCase_data = TestCase.objects.filter(test_run=notepad_id)
    print(TestCase_data)

    context = {'dataTestCase': TestCase_data}
    return render(request, 'webapp/TestCase.html', context)
