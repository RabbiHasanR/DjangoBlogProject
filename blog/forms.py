from django import forms
from blog.models import Post,Comment

class PostForms(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text')

        widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForms(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
