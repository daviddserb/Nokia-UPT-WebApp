from django.shortcuts import render, redirect
from django.contrib import messages  # pop-up messages
from django.contrib.auth import authenticate, login, logout
from webapp.models import TestLine, TestRun, TestCase
from .forms import RegisterUserForm


def home(request):
    return render(request, 'webapp/home.html')


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
    print("! user_profile !")
    # request.user prints only the name (BUT it's not the same as request.user.username), because that's what it only wants to print, but inside it's actually all the information from db
    context = {'userInfo': request.user}
    return render(request, 'webapp/userProfile.html', context)


def favorites_TestLine(request):
    print("@ favorites @")

    # filtrez din interm dar extrag di ntestline
    favorites_id = TestLine.objects.filter(users=request.user)
    print("toate id-urile adaugate la favorite de user-ul logat")
    print(favorites_id)

    context = {'favs_id': favorites_id}
    return render(request, 'webapp/favoritesTestLine.html', context)


def delete_favorites_TestLine(request, notepad_config_id):
    print(" @ delete_favorites_TestLine @")

    # testline = TestLine.objects.all().delete() -> to delete all TestLine (and will delete allso TestRun and TestCase)

    """
    many to many field instance: NameTableWithManyToManyField.NameReferencedTable
    intermediary table model: NameTableWithManyToManyField.NameReferencedTable.through
    intermediary model manager: NameTableWithManyToManyField.NameReferencedTable.through.objects
    return a queryset for all intermediary models: NameTableWithManyToManyField.NameReferencedTable.through.objects.all()
    select = TestLine.users.through.objects.filter(testline_id = notepad_config_id, user_id = request.user.id)
    select.delete()
    """

    testline = TestLine.objects.filter(id=notepad_config_id).first()
    testline.users.remove(request.user)

    return redirect('favorites')


def Testline(request):
    print("! Testline !")
    print("nume user:")
    print(request.user)

    TestLine_data = TestLine.objects.all()

    context = {'dataTestLine': TestLine_data, 'userName': str(request.user)}
    return render(request, 'webapp/TestLine.html', context)


def add_favorites_TestLine(request, notepad_config_id):
    print("# add_favorites_TestLine #")

    # filter() - returns a QuerySet even if only one object is found.
    # get() - returns just one single model instance.
    testline = TestLine.objects.get(id=notepad_config_id)

    print("id-ul care a fost adaugat la favorite de catre user-ul logat:")
    print(testline)

    testline.users.add(request.user)

    print("toti userii care au adaugat la favorite id-ul respectiv:")
    print(testline.users.all())

    return redirect('favorites')


def Testrun(request, notepad_config_id):
    print("( Testrun )")

    # when the user tries manually to put a random number in the path of the page
    if not TestLine.objects.filter(id=notepad_config_id).exists():
        print("NU EXISTA")
        return render(request, 'webapp/404.html')

    Testruns = TestRun.objects.filter(test_line=notepad_config_id)
    print(Testruns)

    passed = []
    failed = []
    for Testrun in Testruns:
        print(Testrun)

        TestCase_lines = TestCase.objects.filter(test_run_id=Testrun.id)
        print(TestCase_lines)

        print("TOTAL:")
        total_tests = TestCase_lines.count()
        print(TestCase_lines.count())

        print("PASS:")
        passed_tests = TestCase_lines.filter(status='PASS').count()
        print(TestCase_lines.filter(status='PASS').count())

        print("FAIL:")
        failed_tests = TestCase_lines.filter(status='FAIL').count()
        print(TestCase_lines.filter(status='FAIL').count())

        print((passed_tests / total_tests) * 100)
        print(format((passed_tests / total_tests) * 100, ".2f"))
        passed.append(format((passed_tests / total_tests) * 100, ".2f"))

        print((failed_tests / total_tests) * 100)
        print(format((failed_tests / total_tests) * 100, ".2f"))
        failed.append(format((failed_tests / total_tests) * 100, ".2f"))

    Testrunes_Testcases = zip(Testruns, passed, failed)
    
    isFavorite = "NO"
    if(str(request.user) != "AnonymousUser"):
        print("y")
        # TestLine.users.through.objects.all() (to go through the entire table)
        # go through the intermediary table (ManyToMany) and search if the logged in user added that testline to his favorites
        TestLine_users = TestLine.users.through.objects.filter(testline_id=notepad_config_id, user_id=request.user)
        print(TestLine_users)

        # check if QuerySet is not empty => the logged in user added that testline to his favorites
        if TestLine_users:
            print("IS NOT EMPTY")
            isFavorite = "YES"

    print(isFavorite)

    context = {'Testcases_details': Testrunes_Testcases, 'notepad_config_id': notepad_config_id, 'userName': str(request.user), 'isFavorite': isFavorite}
    return render(request, 'webapp/TestRun.html', context)


# ordinea parametrilor nu conteaza, trebuie sa aiba aceleasi denumiri cu cele din path si sa fie in acelasi numar
def Testcase(request, notepad_config_id, notepad_id):
    print("* Testcase *")

    print("notepad_config_id:")
    print(notepad_config_id)
    print("notepad_id:")
    print(notepad_id)

    # when the user tries manually to put a random number in the path of the page
    if not TestRun.objects.filter(id=notepad_id).exists():
        print("NU EXISTA")
        return render(request, 'webapp/404.html')

    # select data from table where each TestCase has the id of TestRun
    TestCase_data = TestCase.objects.filter(test_run=notepad_id)
    print(TestCase_data)

    """
    difference between .filter(A, B) VS filter(A).filter(B):
    
    - to extract all blogs from 2008 AND who have "Lennon" as title: .filter(title='Lennon', year=2008).
    - to extract all blogs from 2008 OR who have "Lennon" as title: .filter(title='Lennon').filter(year=2008).
    
    - so .filter(A, B) will first filter EVERYTHING according to A and then subfilter (filter again the RESULT) according to B.
    - while .filter(A).filter(B) will filter EVERYTHING according to A and have a result, and then filter again EVERYTHING and have another result, which may not corespond to the A condition.
    """

    context = {'dataTestCase': TestCase_data}
    return render(request, 'webapp/TestCase.html', context)
