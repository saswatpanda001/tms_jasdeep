from django import forms
from users.models import TrainingProgramModel, UserProfileModel,AppreciationPoints


class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgramModel
        fields = ['name', 'duration', 'skills', 'eligible_positions']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
            'eligible_positions': forms.CheckboxSelectMultiple,
        }




class AppreciationPointsForm(forms.ModelForm):
    class Meta:
        model = AppreciationPoints
        fields = ['receiver', 'points', 'message']

    # Ensure points are greater than 0 and positive
    points = forms.IntegerField(min_value=1, required=True)

