from rest_framework import serializers
from .models import Customer


class CustomerListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'company_name', 'customer_email', 'customer_email', 'work_phone', 'gst_treatment','receivables')



