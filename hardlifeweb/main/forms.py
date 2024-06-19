from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    # original_password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
        # fields = ('username', 'original_password', 'password1', 'password2')
        def save(self, commit=True):
            user = super().save(commit=False)
            user.password = self.cleaned_data['password1']
            if commit:
                user.save()
            return user
