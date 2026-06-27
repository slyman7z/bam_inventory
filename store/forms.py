from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone1', 'phone2', 'email', 'address', 'city', 'state', 'country']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all',
                'placeholder': 'Full name'
            }),
            'phone1': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all',
                'placeholder': '+1 (555) 000-0000'
            }),
            'phone2': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all',
                'placeholder': '+1 (555) 000-0000 (optional)',
                'required': False
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all',
                'placeholder': 'customer@example.com'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all resize-y min-h-[80px]',
                'placeholder': 'Street address',
                'rows': 3
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all',
                'placeholder': 'City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all',
                'placeholder': 'State / Province'
            }),
            'country': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/60 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500/40 focus:border-pink-500/40 transition-all',
                'placeholder': 'Country'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make phone2 optional explicitly
        self.fields['phone2'].required = False
        
        # Add labels for better accessibility
        self.fields['name'].label = 'Full Name'
        self.fields['phone1'].label = 'Primary Phone'
        self.fields['phone2'].label = 'Secondary Phone (Optional)'
        
        # Add help texts
        self.fields['phone1'].help_text = 'Required for contact purposes'
        self.fields['email'].help_text = "We'll never share your email"

    def clean_phone1(self):
        phone = self.cleaned_data.get('phone1')
        # Basic phone validation - remove non-numeric characters
        if phone:
            cleaned = ''.join(filter(str.isdigit, phone))
            if len(cleaned) < 10:
                raise forms.ValidationError('Phone number must have at least 10 digits')
        return phone

    def clean_phone2(self):
        phone2 = self.cleaned_data.get('phone2')
        if phone2:
            cleaned = ''.join(filter(str.isdigit, phone2))
            if len(cleaned) < 10:
                raise forms.ValidationError('Phone number must have at least 10 digits')
        return phone2

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Only check for duplicates if the email is NOT blank or None
        if email and email.strip(): 
            if Customer.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('A customer with this email already exists')
                
        return email