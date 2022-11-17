from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your forms here.

class NewUserForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput)
	password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ("username", "email")

	
 
	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email
		


	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		password_2 = cleaned_data.get("password_2")
		if password is not None and password != password_2:
			self.add_error("password_2", "Your passwords must match")
		return cleaned_data


	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user