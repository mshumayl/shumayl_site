from django import forms 
from .models import Post, Category

#QuerySet object - selection for category
choices = Category.objects.all().values_list('name', 'name')

#Fill QuerySet object into a Python list
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "category", "body", "snippet", "header_image")
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your title here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Select a tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type away!'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provide a snippet for your post'}),
            
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'snippet')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Edit your title here'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Select a tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Edit your content'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provide a snippet for your post'}),
        }
        