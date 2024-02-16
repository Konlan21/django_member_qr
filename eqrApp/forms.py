from secrets import choice
from django import forms
from numpy import require
from eqrApp import models
import qrcode

class SaveEmployee(forms.ModelForm):
    employee_code = forms.CharField(max_length=250, label="Company ID")
    name = forms.CharField(max_length=250, label="Name")
    gender = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female")], label="Gender")
    profession = forms.CharField(max_length=100, label="Profession")
    date_of_birth = forms.DateField(label="Date of Birth")
    date_of_joining_splm = forms.DateField(label="Date of Joining SPLM")
    date_of_issue = forms.DateField(label="Date of Issue")
    expiry_date = forms.DateField(label="Expiry Date")
    avatar = forms.ImageField(label="Avatar", required=False)  # Make it optional
    country = forms.CharField(max_length=255, label="Country")
    state = forms.CharField(max_length=255, label="State")
    payam = forms.CharField(max_length=255, label="Payam")
    boma = forms.CharField(max_length=255, label="Boma")

    class Meta:
        model = models.Member
        fields = ('employee_code',
                  'name',
                  'gender',
                  'profession',
                  'date_of_birth',
                  'date_of_joining_splm',
                  'date_of_issue',
                  'expiry_date',
                  'avatar',
                  'country',
                  'state',
                  'payam',
                  'boma',)

    def clean_employee_code(self):
        id = self.data['id'] if self.data['id'] != '' else 0
        employee_code = self.cleaned_data['employee_code']
        try:
            if id > 0:
                employee = models.Employee.exclude(id=id).get(employee_code = employee_code)
            else:
                employee = models.Employee.get(employee_code = employee_code)
        except:
            return employee_code
        return forms.ValidationError(f"{employee_code} already exists.")

