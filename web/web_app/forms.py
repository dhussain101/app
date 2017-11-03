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
    start_time = forms.DateTimeField(help_text='Format: m/d/y or yyyy-mm-dd hh:mm:ss')
    end_time = forms.DateTimeField(help_text='Format: m/d/y or yyyy-mm-dd hh:mm:ss')

    def clean(self):
        cleaned_data = super(LotteryForm, self).clean()
        if self.is_valid():
            start_time, end_time = map(cleaned_data.get, ('start_time', 'end_time'))
            if end_time <= start_time:
                self.add_error('start_time', 'Cannot start before end date')
        return cleaned_data


class SearchForm(forms.Form):
    q = forms.CharField(max_length=300, label='', required=False)
    lottery = forms.BooleanField(label='lotteries', required=False)
    card = forms.BooleanField(label='cards', required=False)
    title = forms.BooleanField(required=False)
    description = forms.BooleanField(required=False)
    size = forms.IntegerField(initial=5, label='Number of results')

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        # Collect selected indices and fields into lists
        indices = []
        fields = []
        for index in ('lottery', 'card'):
            if cleaned_data.get(index):
                indices.append('{}_index'.format(index))
            if index in cleaned_data:
                del cleaned_data[index]

        for field in ('title', 'description'):
            if cleaned_data.get(field):
                fields.append(field)
            if field in cleaned_data:
                del cleaned_data[field]

        cleaned_data['indices'] = ','.join(indices)
        cleaned_data['fields'] = ','.join(fields)

