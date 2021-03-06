import datetime
from catalog.models import BookInstance
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ 


class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date renewal in the past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date renewal mare than 4 weeks ahead'))
        return data

    class Meta:
        model= BookInstance 
        fields= ['due_back']
        help_texts = {'due_back':_('Enter a date beween ,now and 4 weeks(default3) :')}
        labels= {'due_back':_('Renewal date')}
        
# a function version of the form
"""class RenewBookForm(forms.Form):
    renewal_date= forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data =self.cleaned_data['renewal_date']
    
        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid renewal date in past'))
        
        # check if a date is in allowed range (+4 weeks from today).

        if data > datetime.date.today() + datetime.timedelta(weeks= 4):
            raise ValidationError(_('Invalid date renewal more than 4 weeks ahead.'))
            # Remmember to always return the cleaned data.
        return data"""