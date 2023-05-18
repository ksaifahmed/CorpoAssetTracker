from rest_framework import serializers
from .models import DeviceLog


# serializer for delegating a device to an employee
class DeviceDelegationSerializer(serializers.Serializer):
    device_name = serializers.CharField()
    employee_name = serializers.CharField()

# serializer for returning a device
class DeviceDelegationRemoverSerializer(serializers.Serializer):
    device_name = serializers.CharField()
    employee_name = serializers.CharField()
    return_condition = serializers.CharField()