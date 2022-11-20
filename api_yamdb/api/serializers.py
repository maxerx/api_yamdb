from rest_framework import serializers

from review.models import User, Genre, Category, Title


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


class AdminUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'role')


class NotAdminUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'role')
        read_only_fields = ('role',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id', )


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    genre = GenreSerializer(
        read_only = True,
        many = True
    )
    raiting = serializers.IntegerField(read_only = True)

    class Meta:
        fields = '__all__'
        model = Title

