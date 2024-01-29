from django import forms
from .models import User,BDE,DEVELOPER,Company,Questions,Interview

class UserForm(forms.ModelForm):
  class Meta:
    model=User
    fields='__all__'

class FormBDE(forms.ModelForm):
  class Meta:
    model=BDE
    fields='__all__'

class FormDEVELOPER(forms.ModelForm):
  class Meta:
    model=DEVELOPER 
    fields='__all__'

class FormCompany(forms.ModelForm):
  class Meta:
    model=Company
    fields='__all__'


class FormQuestion(forms.ModelForm):
  class Meta:
    model=Questions
    fields='__all__'


class FormInterview(forms.ModelForm):
  class Meta:
    model=Interview
    fields='__all__'