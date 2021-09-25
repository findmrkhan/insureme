from rest_framework import serializers
from .models import (Quote, Policy, PolicyHistory, PolicyMaster, CurrencyMaster
                        , PolicyStatusMaster, QuoteStatusMaster)

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields = '__all__'
        fields = ( 'id', 'email', 'first_name', 'last_name', 'password', 'dob')


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        # fields = '__all__'
        fields = ('customer', 'policytype', 'quote_status', 'premium', 'max_insured_amount')


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        # fields = '__all__'
        fields = ('customer', 'policy_master', 'effective_date', 'expiry_date', 'premium', 'max_insured_amount')


class PolicyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyHistory
        fields = '__all__'


class PolicyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyMaster
        fields = '__all__'


class CurrencyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyMaster
        fields = '__all__'


class PolicyStatusMasterSerialiser(serializers.ModelSerializer):
    class Meta:
        model = PolicyStatusMaster
        fields = '__all__'


class QuoteStatusMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteStatusMaster
        fields = '__all__'

