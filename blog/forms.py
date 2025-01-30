from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }
