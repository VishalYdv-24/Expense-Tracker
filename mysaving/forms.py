from django import forms
from .models import Expense,Income

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
        widgets = {
            'exp_date': forms.DateInput(attrs={'type': 'date'})
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"
        widgets = {
            'inc_date':forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            )
        }