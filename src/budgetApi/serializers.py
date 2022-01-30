from rest_framework import serializers
from django.contrib.auth.models import User

from budgetApi.models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError('Category already exists')
        return value


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'name', 'type', 'category', 'user']


class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'transactions']
