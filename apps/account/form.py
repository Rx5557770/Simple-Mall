from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    remember = forms.BooleanField(required=False)
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('请传入邮箱')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱不存在')
        return email


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('请传入邮箱')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已存在')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username:
            raise forms.ValidationError('请传入用户名')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('该用户名已存在')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if len(password) < 6:
            raise forms.ValidationError('密码最低为6个字符')

        if password and password2 and password == password2:
            return cleaned_data

        raise forms.ValidationError('表单验证失败')

    def save(self, commit=True):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        if commit:
            user.save()
        return user