from django import forms
from .models import BorrowRecord

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['book']
