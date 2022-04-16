from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
forms.Form
-> trebuie sa fie configurat tot input-ul in totalitate.
-> sunt folosite, de obicei, cand NU interactioneaza cu baza de date.

forms.ModelForm
-> Django ModelForm este o clasa care converteste un model intr-un Django form.

UserCreationForm
-> este folosit pt. a crea noi useri care pot folosi aplicatia.
-> are 3 campuri: username, password1 si password2 (for confirmation).

class Meta
-> follosita pt. a schimba comportamentul campurilor modelului.
-> este o clasa optionala.
"""


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
