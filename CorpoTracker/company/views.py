from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from company.serializers import CompanyRegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout


# Create your views here.
class CompanyRegisterView(APIView):
    def post(self, request):
        serializer = CompanyRegisterSerializer(data=request.data)
        if serializer.is_valid():
            company = serializer.save()
            token, created = Token.objects.get_or_create(user=company.user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyLoginView(APIView):
    def post(self, request):
        name = request.data.get('company_name')
        password = request.data.get('password')

        if name and password:
            user = authenticate(username=name, password=password)
            
            if user is not None:                
                # If the user is authenticated, log them in
                login(request, user)     

                token, _ = Token.objects.get_or_create(user=user)

                request.session['company_id'] = user.company.id

                return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class CompanyLogoutView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):        
        # Perform the logout operation
        logout(request)

        if 'company_id' in request.session:
            del request.session['company_id']

        # Delete the token if user not anonymous
        if not request.user.is_anonymous:
            request.user.auth_token.delete()

        # Flush the session data if exists
        request.session.flush()
        
        return Response(status=status.HTTP_204_NO_CONTENT)