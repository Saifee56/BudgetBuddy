from expense.models import Expense,CustomExpense,Income
from rest_framework import serializers

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Income
        fields=['id','income_type','amount','source','dae_received','note']

    def validate_amount(self,value):
        if value < 0:
            raise serializers.ValidationError('Amount cannot be negative')

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Expense
        fields=['id','expense_type','total_money','note']
    
    def validate_total_money(self,value):
        if value < 0:
            raise serializers.ValidationError('Amount cannot be negative')
    

class CustomExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomExpense
        fields=['id','custom_expense_title','total_money','note']
    
    def validate_total_money(self,value):
        if value < 0:
            raise serializers.ValidationError('Amount cannot be negative')
        