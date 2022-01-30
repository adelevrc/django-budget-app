from django.contrib import admin

# Register your models here.
from budgetApi.models import Category, Transaction

admin.site.register(Category)
admin.site.register(Transaction)
