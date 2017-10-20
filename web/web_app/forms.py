from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, min_length=3)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    remember = forms.BooleanField(label='Remember Me', required=False)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=32, min_length=3, help_text='At least 3 characters')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, help_text='At least 8 characters')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, help_text='Re-enter password')
    birthday = forms.DateField(help_text='Format: m/d/yy')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Password does not match')
        return cleaned_data


class LotteryForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
