from expense.models import Expense
from rest_framework import serializers

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model='Expense'
        fields=['id','expense_type','customer_expense_type','total_money','note']
        