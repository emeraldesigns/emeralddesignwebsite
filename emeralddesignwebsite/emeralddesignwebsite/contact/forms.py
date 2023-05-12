from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=200)
    message = forms.CharField(label='Message', widget=forms.Textarea)
