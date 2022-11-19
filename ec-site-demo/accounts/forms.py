from django import forms
from allauth.account.forms import SignupForm

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='性')
    last_name = forms.CharField(max_length=30, label='名')
    address = forms.CharField(max_length=30, label='住所')
    tel = forms.CharField(max_length=30, label='電話番号')
    
class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='性')
    last_name = forms.CharField(max_length=30, label='名')
    
    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
        return user