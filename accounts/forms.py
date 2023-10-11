from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    firstName = forms.CharField(max_length=254, required=True)
    secondName = forms.CharField(max_length=254, required=True)
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields["password1"].widget.attrs.update({
    #         'required':'',
    #         'name':'password1',
    #         'id':'password1',
    #         'type': 'password',
    #         'class': 'form-input',
    #         'autocomplete': 'on'
    #     })
    class Meta:
        model = User
        fields = ('firstName', 'secondName', 'email', 'username', 'password1', 'password2')

