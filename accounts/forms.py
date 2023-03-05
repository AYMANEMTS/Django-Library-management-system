from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2','phone')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user






class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','password')
