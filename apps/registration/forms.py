from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Обязательное поле. Введите рабочий Email адрес.')

    first_name = forms.CharField(max_length=50, required=True, label='Имя', help_text='Обязательное поле. '
                                                                                      'Не более 50 символов. '
                                                                                      'Только буквы, цифры и символы.')

    last_name = forms.CharField(max_length=50, required=True, label='Фамилия', help_text='Обязательное поле. '
                                                                                         'Не более 50 символов. '
                                                                                         'Только буквы, цифры и '
                                                                                         'символы. '
                                )

    class Meta:
        model = User
        fields = ["username", "email", 'first_name', 'last_name', "password1", "password2"]
