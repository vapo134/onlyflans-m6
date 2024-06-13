from django import forms

class ContactFormForm(forms.Form):
    
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    
    
    