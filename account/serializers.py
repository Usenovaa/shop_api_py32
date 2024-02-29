from rest_framework import serializers
from django.contrib.auth import get_user_model
# from .utils import send_activation_code
from .tasks import send_activation_code_celery


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model = User
        fields = 'email', 'password', 'password_confirm'

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError(
                'Passwords don\'t match'
            )
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code_celery.delay(user.email, user.activation_code)
        return user
    
'''
python3 -m celery -A config worker -l info
'''
