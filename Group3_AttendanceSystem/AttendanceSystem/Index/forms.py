from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Student.models import Student
from Teacher.models import Teacher


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'formfield','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'formfield','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formfield', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']


class CreateStudentForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'formfield', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'formfield', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'formfield', 'placeholder': 'Confirm Password'}))
    course = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Course (ex. BSIT)'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'formfield', 'placeholder': 'Year', 'min': '1','max': '6'}))

    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2', 'course', 'year']


class CreateTeacherForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'formfield', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'formfield', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'formfield', 'placeholder': 'Confirm Password'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Department'}))

    class Meta:
        model = Teacher
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2', 'department']
