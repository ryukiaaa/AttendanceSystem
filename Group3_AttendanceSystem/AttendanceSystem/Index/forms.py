from django import forms
from Student.models import Student
from Teacher.models import Teacher


class CreateStudentForm(forms.ModelForm):
    courses = [
        ('', 'Select Course'),
        ('BSIT', 'BS Information Technology'),
        ('BSCS', 'BS Computer Science'),
        ('BSN', 'BS Nursing'),
        ('BSP', 'BS Pharmacy'),
    ]

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'formfield', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'formfield', 'placeholder': 'Password'}))
    course = forms.ChoiceField(choices=courses, widget=forms.Select(attrs={'class': 'formfield'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'formfield', 'placeholder': 'Year', 'min': '1','max': '6'}))

    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'course', 'year']


class CreateTeacherForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'formfield', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'formfield', 'placeholder': 'Password'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Department'}))
    type = forms.CharField(initial='T', widget=forms.HiddenInput())

    class Meta:
        model = Teacher
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'department','type']