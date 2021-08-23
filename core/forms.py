from django import forms

from .models import ContactModel

# class ContactForm(forms.Form):
#     first_name= forms.CharField(max_length=500, label="first_name")
#     last_name= forms.CharField(max_length=500, label="last_name")
#     email = forms.EmailField(max_length=500, label="email")
#     message = forms.CharField(label='',widget=forms.Textarea(
#                         attrs={'placeholder': 'Enter your comment here','rows':7 ,'cols':50}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'message']
        

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control','rows':7})
        }
    
