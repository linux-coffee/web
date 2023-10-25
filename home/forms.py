from django.forms import ModelForm
from django import forms
from .models import Home,Comment


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    discriptions = forms.CharField()
    body = forms.CharField()
    author = forms.CharField()
    img = forms.ImageField()
    created = forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')