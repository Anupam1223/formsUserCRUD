from django import forms
from django.core.exceptions import ValidationError
from user.models import User
from django.contrib.auth.hashers import (
    check_password,
)

# class for login form
class LoginForm(forms.Form):

    email = forms.EmailField(
        error_messages={"required": ""},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Email",
            }
        ),
    )

    password = forms.CharField(
        error_messages={"required": ""},
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password", "class": "password"}
        ),
    )
    rememberMe = forms.CharField(
        widget=forms.CheckboxInput(
            attrs={
                "id": "rememberMe",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()

        valEmail = self.cleaned_data.get("email")

        if not valEmail:
            raise ValidationError("please enter Email")

        valpassword = self.cleaned_data.get("password")

        if not valpassword:
            raise ValidationError("please enter password")

        verifyUser = User.objects.filter(email=valEmail).first()

        if not verifyUser:
            raise ValidationError("user doesn't exists")

        if not verifyUser.is_active:
            raise ValidationError("user is not active, check your mail")

        if not check_password(valpassword, verifyUser.password):
            raise ValidationError("username and  password didnt matched")


# different class for password change
class ChangePassForm(forms.Form):

    email = forms.EmailField(
        error_messages={"required": "please enter Email"},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Email",
            }
        ),
    )
