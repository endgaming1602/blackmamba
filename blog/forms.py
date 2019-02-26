from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    title       = forms.CharField(required=True, widget=forms.TextInput(attrs={
                                                                            "placeholder": "Title",
                                                                            "class":"form-control",
                                                                            "name":"name",
                                                                            "id":"id_title"
                                                                            }))
    text        = forms.CharField(required=True, widget=forms.Textarea(attrs={
                                                                            "name":"name",
                                                                            "placeholder":"description",
                                                                            "class":"form-control no-resize",
                                                                            "cols":30,
                                                                            "rows":5,
                                                                            "id":"id_text"
                                                                            }))
    class Meta:
        model = Post
        fields = ['title', 'text']
