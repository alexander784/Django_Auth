from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.



@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return JsonResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.validated_data['user']

    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh':str(refresh),
        'access':str(refresh.access_token),
        'user':UserSerializer(user).data
    }, status=status.HTTP_200_OK)