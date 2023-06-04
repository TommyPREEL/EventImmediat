from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from EventImmediatApp.models import Events
from django.forms.widgets import DateInput

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=63, label='Username')
    last_name = forms.CharField(max_length=63, label='Last name')
    first_name = forms.CharField(max_length=63, label='First name')
    email = forms.CharField(max_length=63, label='Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'last_name', 'first_name', 'email')

class DateInputWidget(DateInput):
    input_type = 'date'

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title', 'description', 'status', 'date_start', 'date_end')
        widgets = {
            'date_start': DateInputWidget(),
            'date_end': DateInputWidget()
        }