from django.contrib.auth.models import User, Permission
from rest_framework import generics, permissions, viewsets, status

from budgetApi.models import Category, Transaction
from budgetApi.serializers import CategorySerializer, TransactionSerializer, UserSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(user=user)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(user=user)

