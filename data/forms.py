from django import forms
from data.models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'class':'name'}),
     error_messages= {'required':"Name is required"})
    # image = forms.ImageField(widget= forms.ImageField(),
    #  error_messages= {'required':"image is required"})
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'email'}),
     error_messages= {'required':"Email  is required"})
    password = forms.CharField(widget= forms.PasswordInput(render_value=True, attrs={'class':'pass'}),
     error_messages= {'required':"Password is required"})
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']