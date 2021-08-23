from django import forms

from .models import Post, Category, Comment
# from mptt.forms import TreeNodeChoiceField

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


class CommentForm(forms.ModelForm):
    # parent = TreeNodeChoiceField(queryset=Comment.objects.all(),required=False)

    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'comment'}),
        }
