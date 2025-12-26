from django.db import models

# Create your models here.
class Expense(models.Model):
    
    exp_desc = models.CharField(max_length=150)
    exp_amount = models.DecimalField(max_digits=10,decimal_places=2)
    exp_date = models.DateField()

    def __str__(self):
        return f"{self.exp_desc} : ₹{self.exp_amount}"
    

class Income(models.Model):

    inc_desc = models.CharField(max_length=150)
    inc_amount = models.DecimalField(max_digits=10,decimal_places=2)
    inc_date = models.DateField()

    def __str__(self):
        return f"{self.inc_desc} : ₹{self.inc_amount}"