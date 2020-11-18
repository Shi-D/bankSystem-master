from django import forms

class DepositForm(forms.Form):
    typeList=(
        ('current', "活期"),
        ('regular', "定期"),
        ('fix', "定活期"),
    )
    timeList=(
        ('')
    )

    cardPassword = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    money = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    types = forms.CharField(choices=typeList)
    time = forms.CharField(choices=timeList)