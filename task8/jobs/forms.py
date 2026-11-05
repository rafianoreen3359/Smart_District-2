from django import forms
from .models import Job, Application


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ['company', 'created_at']

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title.strip()) < 3:
            raise forms.ValidationError(
                "Job title must contain at least 3 characters."
            )

        return title.strip()

    def clean_description(self):
        description = self.cleaned_data.get('description')

        if len(description.strip()) < 20:
            raise forms.ValidationError(
                "Description must contain at least 20 characters."
            )

        return description.strip()

    def clean_location(self):
        location = self.cleaned_data.get('location')

        if not location.strip():
            raise forms.ValidationError("Location is required.")

        return location.strip()

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')

        if salary is not None and salary <= 0:
            raise forms.ValidationError(
                "Salary must be greater than zero."
            )

        return salary


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['cover_letter']

    def clean_cover_letter(self):
        letter = self.cleaned_data.get('cover_letter')

        if len(letter.strip()) < 30:
            raise forms.ValidationError(
                "Cover letter must contain at least 30 characters."
            )

        return letter.strip()