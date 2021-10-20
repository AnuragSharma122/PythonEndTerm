from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields =('content')