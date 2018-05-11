from django import forms
from hc.blog.models import BlogCategory,BlogPost



class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model=BlogCategory
        fields=('title',)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields = ('category', 'title','content')
                      