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


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import password_validation  # Import password_validation
# from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     password1 = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         help_text=password_validation.password_validators_help_text_html(),
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password2'].help_text = "Enter the same password as before, for verification."
#         self.fields['password2'].widget.attrs.update({'class': 'form-control'})

