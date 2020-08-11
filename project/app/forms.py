from django import forms

class NameForm(forms.Form):
    UserName = forms.CharField(label='Username', max_length=100)
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
