from rest_framework import serializers

from review.models import  Genre, Category, Title


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


