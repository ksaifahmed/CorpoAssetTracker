from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer
from .models import Device
from company.models import Company


class DeviceCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        device_names = [data['device_name'] for data in serializer.validated_data]
        status_of_devices = [data['status'] for data in serializer.validated_data]

        existing_devices = []
        created_devices = []

        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)
        
        # enumerate through device names and status
        for name, status in zip(device_names, status_of_devices):
            device = Device.objects.filter(device_name=name, company=company).first()
            if device:
                existing_devices.append(device)
            else:
                created_device = Device.objects.create(device_name=name, status=status, company=company)
                created_devices.append(created_device)


        response_data = {
            'new devices added': DeviceSerializer(created_devices, many=True).data,
            'these devices already exist': DeviceSerializer(existing_devices, many=True).data,
        }
        return Response(response_data)
    

class DeviceListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)        
        devices = company.devices()

        serializer = DeviceSerializer(devices, many=True)
        
        return Response(serializer.data)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer
from .models import Device
from company.models import Company


class DeviceCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        device_names = [data['device_name'] for data in serializer.validated_data]
        status_of_devices = [data['status'] for data in serializer.validated_data]

        existing_devices = []
        created_devices = []

        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)
        
        # enumerate through device names and status
        for name, status in zip(device_names, status_of_devices):
            device = Device.objects.filter(device_name=name, company=company).first()
            if device:
                existing_devices.append(device)
            else:
                created_device = Device.objects.create(device_name=name, status=status, company=company)
                created_devices.append(created_device)


        response_data = {
            'new devices added': DeviceSerializer(created_devices, many=True).data,
            'these devices already exist': DeviceSerializer(existing_devices, many=True).data,
        }
        return Response(response_data)
    

class DeviceListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)        
        devices = company.devices()

        serializer = DeviceSerializer(devices, many=True)
        
        return Response(serializer.data)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer
from .models import Device
from company.models import Company


class DeviceCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        device_names = [data['device_name'] for data in serializer.validated_data]
        status_of_devices = [data['status'] for data in serializer.validated_data]

        existing_devices = []
        created_devices = []

        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)
        
        # enumerate through device names and status
        for name, status in zip(device_names, status_of_devices):
            device = Device.objects.filter(device_name=name, company=company).first()
            if device:
                existing_devices.append(device)
            else:
                created_device = Device.objects.create(device_name=name, status=status, company=company)
                created_devices.append(created_device)


        response_data = {
            'new devices added': DeviceSerializer(created_devices, many=True).data,
            'these devices already exist': DeviceSerializer(existing_devices, many=True).data,
        }
        return Response(response_data)
    

class DeviceListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)        
        devices = company.devices()

        serializer = DeviceSerializer(devices, many=True)
        
        return Response(serializer.data)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer
from .models import Device
from company.models import Company


class DeviceCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        device_names = [data['device_name'] for data in serializer.validated_data]
        status_of_devices = [data['status'] for data in serializer.validated_data]

        existing_devices = []
        created_devices = []

        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)
        
        # enumerate through device names and status
        for name, status in zip(device_names, status_of_devices):
            device = Device.objects.filter(device_name=name, company=company).first()
            if device:
                existing_devices.append(device)
            else:
                created_device = Device.objects.create(device_name=name, status=status, company=company)
                created_devices.append(created_device)


        response_data = {
            'new devices added': DeviceSerializer(created_devices, many=True).data,
            'these devices already exist': DeviceSerializer(existing_devices, many=True).data,
        }
        return Response(response_data)
    

class DeviceListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)        
        devices = company.devices()

        serializer = DeviceSerializer(devices, many=True)
        
        return Response(serializer.data)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer
from .models import Device
from company.models import Company


class DeviceCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        device_names = [data['device_name'] for data in serializer.validated_data]
        status_of_devices = [data['status'] for data in serializer.validated_data]

        existing_devices = []
        created_devices = []

        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)
        
        # enumerate through device names and status
        for name, status in zip(device_names, status_of_devices):
            device = Device.objects.filter(device_name=name, company=company).first()
            if device:
                existing_devices.append(device)
            else:
                created_device = Device.objects.create(device_name=name, status=status, company=company)
                created_devices.append(created_device)


        response_data = {
            'new devices added': DeviceSerializer(created_devices, many=True).data,
            'these devices already exist': DeviceSerializer(existing_devices, many=True).data,
        }
        return Response(response_data)
    

class DeviceListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)        
        devices = company.devices()

        serializer = DeviceSerializer(devices, many=True)
        
        return Response(serializer.data)
