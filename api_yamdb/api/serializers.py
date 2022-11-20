from rest_framework import serializers
from review.models import User


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code'
        )

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')
    
    def validate(self, data):
        if data['username'] == "me":
            raise serializers.ValidationError(
                'Нельзя использовать в качестве имени Me')
        return data