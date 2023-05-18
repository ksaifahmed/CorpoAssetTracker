from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DeviceLog
from company.models import Company
from employee.models import Employee
from device.models import Device
from .serializers import *
import datetime


# Delegate devices to employees ===========================================================================
class DeviceDelegationCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceDelegationSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        employee_names = [data['employee_name'] for data in serializer.validated_data]
        device_names = [data['device_name'] for data in serializer.validated_data]


        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)

        # enumerate through device names and employee names
        # if device name exists and employee name exists, then create a new device log
        not_found_devices = []
        not_found_employees = []
        devices_delegated = []

        for device, employee in zip(device_names, employee_names):
            device_object = Device.objects.filter(device_name=device, company=company, in_use=False).first()
            employee_object = Employee.objects.filter(employee_name=employee, company=company).first()

            if not device_object:
                not_found_devices.append(device)
            if not employee_object:
                not_found_employees.append(employee)
            elif device_object and employee_object:
                # get device status
                device_status = device_object.status
                # get current date and time
                date_ = datetime.datetime.now()
                
                DeviceLog.objects.create(
                    device=device_object, employee=employee_object,
                    condition=device_status, check_out_at=date_
                )

                # update device in_use field to True
                device_object.in_use = True
                device_object.save()

                # {"device_name": "device1", "employee_name": "employee1"}
                devices_delegated.append({"device_name": device, "employee_name": employee})


        response_data = {
            "devices_delegated": devices_delegated,
            "not_found_or_unavailable_devices": not_found_devices,
            "not_found_employees": not_found_employees
        }     

        return Response(response_data)

# end of DeviceDelegationCreateView =======================================================================



# Return list of all delegations of devices to employees of current company ==============================
# shows status, condition, device name, employee name, check out time, return time, return condition
# of all devices delegated to employees of current company
class DeviceDelegationsListView(APIView):
    # permission_classes = [IsAuthenticated]

    # list of all delegations of devices to employees of current company
    def get(self, request):
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)

        # get all device logs of current company
        device_logs = DeviceLog.objects.filter(device__company=company)

        # data from device logs in a single list
        device_logs_data = []
        for device_log in device_logs:
            device_logs_data.append({
                "device_name": device_log.device.device_name,
                "employee_name": device_log.employee.employee_name,
                "check_out_at": device_log.check_out_at,
                "return_at": device_log.return_at,
                "condition": device_log.condition,
                "return_condition": device_log.return_condition
            })

        return Response(device_logs_data)

# end of DeviceDelegationsListView =========================================================================



# Return a Device from One Employee back to Company ========================================================
# TODO: ASSUMPTION: DEVICES ARE RETURNED ONE BY ONE AND THE RETURN CONDITION IS CHECKED BY HAND
class DeviceDelegationRemoverView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        serializer = DeviceDelegationRemoverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        employee_name = data['employee_name']
        device_name = data['device_name']

        # check if employee exists
        employee = Employee.objects.filter(employee_name=employee_name).first()

        # return error message if employee does not exist
        if not employee:
            return Response({'error': 'Employee does not exist'}, status=400)
        
        # check if device exists
        device = Device.objects.filter(device_name=device_name).first()

        # return error message if device does not exist
        if not device:
            return Response({'error': 'Device does not exist'}, status=400)
        
        # check if device is in use
        if not device.in_use:
            return Response({'error': 'Device is not in use'}, status=400)
        
        # check if device is delegated to employee and not returned yet
        device_log = DeviceLog.objects.filter(device=device, employee=employee, return_at=None).first()

        # return error message if device is not delegated to this employee
        if not device_log:
            return Response({'error': 'Device is not delegated to this employee'}, status=400)
        
        # get current date and time
        date_ = datetime.datetime.now()

        # update device log
        device_log.return_at = date_        
        device_log.return_condition = data['return_condition']
        device_log.save()

        # update device in_use field to False and update device status
        device.in_use = False
        device.status = data['return_condition']
        device.save()        

        return Response({'success': 'Device returned successfully'})

    
# end of DeviceDelegationRetrieveView =====================================================================