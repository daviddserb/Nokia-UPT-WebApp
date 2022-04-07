from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
forms.Form
-> trebuie sa fie configurat in totalitate (adica sa declar ce vreau la input).
-> sunt folosite, de preferat, cand NU interactioneaza cu models (baza de date).

forms.ModelForm
-> Django ModelForm este o clasa, care este folosita pt. a crea un HTML form folosind Model.

UserCreationForm
-> este folosit pt. a crea noi useri care pot folosi aplicatia.
-> are 3 campuri: username, password1 si password2 (=password confirmation)

class Meta
-> Model Meta este clasa interioara a clasei model.
-> Model Meta este follosit pt. a schimba comportamentul campurilor modelului (de ex. ordinea campurilor).
-> este o clasa optionala.
"""

# de testing
class NameForm(forms.Form):
    name = forms.CharField(max_length=100)
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()


class RegisterUserForm(UserCreationForm):

    # class Meta gives us a nested namespaces for configurations and keeps the configurations in one place and within the configuration we are saying that the model that will be affected is the User model (because model = User)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']