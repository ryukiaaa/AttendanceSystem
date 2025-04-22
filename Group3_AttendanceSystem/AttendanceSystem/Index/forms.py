from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'formfield','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Student registration form
class StudentRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'formfield','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Confirm Password'}))
    student_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Student ID'}))
    course = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Course'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'formfield','placeholder':'Year Level'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Teacher registration form
class TeacherRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'formfield','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Confirm Password'}))
    department_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Department ID'}))
    courses = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Courses'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
