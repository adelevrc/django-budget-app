from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    # tye type of email attribute is an EmailField and that it is required and should be unique amongst all User objects
    # in our database
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # write_only
    # Set this to True to ensure that the field may be used when updating or creating an instance,
    # but is not included when serializing the representation.

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # These are the fields that our registration form is contains :
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

        # These are the fields that our registration form is contains.
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    # Password fields must be same. We can validate these fields with serializers validate(self, attrs) method:
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    # Password fields must be same. We can validate these fields with serializers validate(self, attrs) method:

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


