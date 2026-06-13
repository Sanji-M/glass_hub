from django import forms

class SignupForm(forms.Form):
    full_name = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)


#validation for the form
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match.')
    
        if p1 and len(p1) < 6:
            raise forms.ValidationError('password must be at least 6 characters long.')
        return cleaned_data
    
    
