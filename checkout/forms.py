from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        fields = ('full_name', 'email', 'phone_number',
                    'street_address1', 'street_address2', 'town_or_city',
                    'postcode', 'country', 'county',)

    def __init__(self, *args, **kwargs):
        """
        Enable better editing 
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Contact Number',
            'country': 'Country',
            'postcode': 'Post Code',
            'town_or_city': 'City',
            'street_address1': 'Line 1 of Address',
            'street_address2': 'Line 2 of Address',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'placeholder[field] *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'field-style'
            self.fields[field].label = False