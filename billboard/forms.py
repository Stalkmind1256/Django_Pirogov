from django import forms
from .models import Billboard

class BillboardForm(forms.ModelForm):

    class Meta:
        model = Billboard
        fields = ('title', 'text')