from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)
    phone = forms.IntegerField(label='Номер телефона', widget=forms.NumberInput, required=False)

    class Meta:
        model = User
        fields = ('username', 'email',)
        labels = {
            'username': ('Ваш никнейм'),
            'email': ('Ваша почта'),
        }
        widgets = {
            'any_proof':forms.ClearableFileInput(attrs={
                'class': "form-control",
                'style':'width:10%;border:1px solid #ced4da;',
                })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']