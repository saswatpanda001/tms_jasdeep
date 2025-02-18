from django import forms
from .models import UserProfileModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = [
            "phone_number", "address", "skills", "certifications", "achievements", 
            "trainings", "rating", "experience_years", "position", "position_gen", 
            "notifications_enabled", "image"
        ]
        widgets = {
            "phone_number": forms.TextInput(attrs={"placeholder": "Enter phone number", "class": "input-field"}),
            "address": forms.Textarea(attrs={"rows": 3, "class": "input-field"}),
            "skills": forms.SelectMultiple(attrs={"class": "input-field"}),
            "certifications": forms.SelectMultiple(attrs={"class": "input-field"}),
            "achievements": forms.SelectMultiple(attrs={"class": "input-field"}),
            "trainings": forms.SelectMultiple(attrs={"class": "input-field"}),
            "rating": forms.NumberInput(attrs={"class": "input-field"}),
            "experience_years": forms.NumberInput(attrs={"class": "input-field"}),
            "position": forms.Select(attrs={"class": "input-field"}),
            "position_gen": forms.TextInput(attrs={"class": "input-field"}),
            "notifications_enabled": forms.CheckboxInput(attrs={"class": "toggle-checkbox"}),
            "image": forms.FileInput(attrs={"class": "file-input"}),
        }
