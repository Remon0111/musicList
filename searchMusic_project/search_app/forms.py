from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Music
from django.contrib.auth.models import User

class CreateMenuForm(forms.ModelForm):
    class Meta:
        # CafeMenuモデルの項目を引用
        model = Music
        fields = ('musicname', 'musicvocalist', 'musicimages', 'albumname', 'musicurl', "musicselect")


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SearchForm(forms.Form):
    keyword = forms.CharField(
        label='検索',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'キーワードを入力'})
    )