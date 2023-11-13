from django import forms
from .models import Student


class SignUPForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["username", "password", "phone_number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def clean(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if confirm_password != password:
            raise forms.ValidationError("Passwords must match!")

