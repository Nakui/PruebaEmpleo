from django import forms
from inCharge.models import InCharge

class InChargeForm(forms.ModelForm):

    class Meta:
        model = InCharge
        fields = [
            'inChargeName',
        ]

        labels = {
            'inChargeName': 'In Charge Name',

        }

        widgets = {
            'inChargeName': forms.TextInput(attrs={'class': 'form-control'}),
        }