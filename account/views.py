from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Successfully registered', status=201)

class ActivateView(APIView):
    def get(self, request, email, activation_code):
        user = get_user_model().objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('Пользователь не найден', 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', 200)


