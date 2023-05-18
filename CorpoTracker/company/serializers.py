from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Company
        fields = ('user', 'company_name', 'employees', 'devices')


class CompanyRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Company
        fields = ('company_name', 'password')

    def create(self, validated_data):
        # check if user exists
        if User.objects.filter(username=validated_data['company_name']).exists():
            raise serializers.ValidationError({'company_name': 'This name is already taken'})
        
        user = User.objects.create_user(
            username=validated_data['company_name'],
            password=validated_data['password']
        )
        company = Company.objects.create(
            user=user,
            company_name=validated_data['company_name']
        )
        return company
