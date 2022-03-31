from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
forms.Form
-> sunt configurate de mine.
-> sunt de preferat sa fie folosite cand NU interactioneaza cu models (baza de date).
-> ex. un formular de contact/abonare la newsletter, in care s-ar putea sa nu trebuiasca
sa interctionezi neaparat cu baza de date.

forms.ModelForm
-> va fi creat automat și apoi poate fi modificat de dvs.

UserCreationForm
-> este folosit pt. a crea noi useri care pot folosi aplicatia.
-> are 3 campuri: username, password1 si password2 (=password confirmation)

class Meta
"""

class NameForm(forms.Form):
    print("se intra in NameForm")
    your_name = forms.CharField(label='Your name', max_length=100)

class RegisterUserForm(UserCreationForm):
    print("$$$ forms.py/CreateUserForm $$$")
    # class Meta gives us a nested namespaces for configurations and keeps the configurations in one place and within the configuration we are saying that the model that will be affected is the User model (because model = User)
    class Meta:
        print("Meta")
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        