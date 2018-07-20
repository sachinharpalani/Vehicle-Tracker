from django import forms
from .models import Report

class UploadReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('xml_file',)
