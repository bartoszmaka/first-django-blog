from django import forms
from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=32)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_retyped = forms.CharField(widget=forms.PasswordInput())

    def add(self):
        new_user = User.objects.create_user(self.cleaned_data['username'],
                                            self.cleaned_data['email'],
                                            self.cleaned_data['password'])
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.save()
