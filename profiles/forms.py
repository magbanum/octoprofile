from django import forms


class UsernameForm(forms.Form):
    username = forms.CharField(label='Find your Github Profile', label_suffix="", max_length=100,
                               widget=forms.TextInput(attrs={'id': 'username-input', 'autofocus': ''}))
