from django import forms
from datetime import date
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
            "full_name",
            "dob",
            "email",
            "glucose",
            "haemoglobin",
            "cholesterol",
        ]

        widgets = {
            "dob": forms.DateInput(
                attrs={
                    "type": "date",
                    "max": date.today().isoformat(),
                    "class": "form-control",
                },
                format="%Y-%m-%d",
            ),
        }

    def clean_dob(self):
        dob = self.cleaned_data["dob"]
        if dob > date.today():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob

    def clean_full_name(self):
        name = self.cleaned_data["full_name"].strip()
        if len(name) < 3:
            raise forms.ValidationError("Name must contain at least 3 characters.")
        return name

    def clean_glucose(self):
        glucose = self.cleaned_data["glucose"]
        if glucose <= 0:
            raise forms.ValidationError("Glucose must be greater than 0.")
        return glucose

    def clean_haemoglobin(self):
        hb = self.cleaned_data["haemoglobin"]
        if hb <= 0:
            raise forms.ValidationError("Haemoglobin must be greater than 0.")
        return hb

    def clean_cholesterol(self):
        cholesterol = self.cleaned_data["cholesterol"]
        if cholesterol <= 0:
            raise forms.ValidationError("Cholesterol must be greater than 0.")
        return cholesterol