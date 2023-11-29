from django import forms

from main_app.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            "dob": forms.DateInput(attrs={"min": "1990-01-01", "max": "1999-12-31"}),
            "kcpe_score": forms.NumberInput(attrs={"max": 500, "min": 0})
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
