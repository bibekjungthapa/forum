from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    # your_name = forms.CharField(label='Username', max_length=100)
    class Meta:
        model = User
        fields = ("username","password")
        def save(self, commit=True):
            user = super(LoginForm, self).save(commit=False)
            return user

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
    
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user