from django import forms
from django.forms import ModelForm

from authentication.models import User


class SignUpForm(ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "signin_input",
                "type": "password",
                "id": "password",
                "name": "Password1",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("email", "name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {
                "class": "signin_input",
                "type": "email",
                "id": "email",
                "name": "Email",
            }
        )
        self.fields["name"].widget.attrs.update(
            {
                "class": "signin_input",
                "type": "text",
                "id": "name",
                "name": "Name",
            }
        )

    def save(self, commit=True):
        """
        Save the user, if commit is True
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")
