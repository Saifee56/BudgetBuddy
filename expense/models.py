from django.db import models

# Create your models here.
class Expense(models.Model):

    EXPENSE_CHOICES=[
    ('shopping','SHOPPING'),
    ('Food','FOOD'),
    ('Phone','PHONE'),
    ('Entertainment','ENTERTAINMENT'),
    ('Education','EDUCATION'),
    ('Health','HEALTH')]

    expense_type=models.CharField(
        max_length=30,
        choices=EXPENSE_CHOICES,
        null=True,
        blank=True,
        help_text="Select from predefined categories"
    )
    custom_expense_type=models.CharField(
        max_length=40,
        null=True,
        blank=True,
        help_text="Enter your custom category if not listed there"
    )
    total_money=models.BigIntegerField()
    note=models.TextField(max_length=255)
    class Meta:
        verbose_name='Expense'
        verbose_name_plural='Expenses'

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.expense_type and not self.custom_expense_type:
            raise ValidationError('You must select an expense type or enter a custom one')
    
    def __str__(self):
        return f'{self.expense_type}--->{self.total_money}'
        