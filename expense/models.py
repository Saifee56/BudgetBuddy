from django.db import models

# Create your models here.

class Income(models.Model):
    INCOME_CHOICES = [
        ('salary', 'Salary'),
        ('business', 'Business'),
        ('freelance', 'Freelance'),
        ('rental', 'Rental'),
        ('investment', 'Investment'),
    ]
    income_type = models.CharField(max_length=30, choices=INCOME_CHOICES, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    source = models.CharField(max_length=100, null=True, blank=True)
    date_received = models.DateField()
    note = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Income'
        verbose_name_plural='Incomes'

    def __str__(self):
        return f'{self.income_type}-->{self.amount}'

    

class Expense(models.Model):

    EXPENSE_CHOICES=[
    ('shopping','SHOPPING'),
    ('Food','FOOD'),
    ('Phone','PHONE'),
    ('Entertainment','ENTERTAINMENT'),
    ('Education','EDUCATION'),
    ('Health','HEALTH')]

    income=models.ForeignKey(Income,null=True,blank=True,on_delete=models.CASCADE)
    expense_type=models.CharField(
        max_length=30,
        choices=EXPENSE_CHOICES,
        null=True,
        blank=True,
        help_text="Select from predefined categories"
    )
    total_money=models.BigIntegerField()
    note=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Expense'
        verbose_name_plural='Expenses'

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.expense_type:
            raise ValidationError('You must select an expense type')
    
    def __str__(self):
        return f'{self.expense_type}--->{self.total_money}'

class CustomExpense(models.Model):
    income=models.ForeignKey(Income,null=True,blank=True,on_delete=models.CASCADE)
    custom_expense_title=models.CharField(max_length=100,null=True,blank=True,on_delete=models.CASCADE)
    total_money=models.BigIntegerField()
    note=models.TextField(max_length=255)

    def __str__(self):
        return f'{self.custom_expense_title}-----> {self.total_money}'
        