from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Pushes, CustomUser, Options


class OptionsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Укажите имя', 'class': 'form-control'}))
    value = forms.BooleanField(required=False,
                               widget=forms.CheckboxInput(attrs={'class': 'custom-control-checkbox'}))

    class Meta:
        model = Options
        fields = ('name', 'value')


class PushesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'id'  : 'push-title', 'placeholder': 'Укажите заголовок'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Укажите заголовок'}))
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'placeholder': 'Пример: http://yourapp.com/image.png', 'id': 'image-push', }))
    sent_date = forms.DateTimeField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YY'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'push-name'}))

    class Meta:
        model = Pushes
        fields = ('title', 'text', 'image', 'sent_date', 'name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'image', 'last_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(attrs={'class': 'custom-control-checkbox'}))
