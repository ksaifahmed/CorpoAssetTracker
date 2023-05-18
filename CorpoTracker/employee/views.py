from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee
from company.models import Company


# Add new employees, names are assumed unique per company
# employee names are unique for a company (no duplicates for the same company)
# for simplificiation purposes
class EmployeeCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        employee_names = [data['employee_name'] for data in serializer.validated_data]
        existing_employees = []
        created_employees = []

        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)
        
        for name in employee_names:
            employee = Employee.objects.filter(employee_name=name, company=company).first()
            if employee:
                existing_employees.append(employee)
            else:
                created_employee = Employee.objects.create(employee_name=name, company=company)
                created_employees.append(created_employee)

        response_data = {}

        response_data = {
            'new employees added': EmployeeSerializer(created_employees, many=True).data,
            'employees already exist': EmployeeSerializer(existing_employees, many=True).data,
        }
        return Response(response_data)


# List all employees for a company
class EmployeeListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if 'company_id' not in request.session:
            return Response({'error': 'Company not logged in'}, status=400)
        
        company_id = request.session['company_id']
        company = Company.objects.get(id=company_id)
        
        employees = Employee.objects.filter(company=company)
        serializer = EmployeeSerializer(employees, many=True)
        
        return Response(serializer.data)