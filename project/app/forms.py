from django import forms

class NameForm(forms.Form):
    UserName = forms.CharField(label='Username', max_length=100)
