from django.contrib import admin
from expense.models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display=('id','expense_type','customer_expense_type',
                  'total_money','note')
