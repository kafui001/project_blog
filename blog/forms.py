from django import forms

from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

# category_choice = [('Python','Python'),('Django','Django'),('JavaScript','JavaScript')]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'post title'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'category': forms.Select(choices=category_choice, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
