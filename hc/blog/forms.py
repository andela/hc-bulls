from django import forms
from hc.blog.models import BlogCategory,BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields = ('title', 'content',)
        widgets={
            'category':forms.CheckboxInput()
        }

class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model=BlogCategory
        fields=('title',)        