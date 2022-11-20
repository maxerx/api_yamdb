from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from rest_framework import permissions, status, viewsets
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAdminUserOrReadOnly, IsAdmin
from review.models import User, Category, Genre, Title

from api.serializers import (GenreSerializer, CategorySerializer, AdminUsersSerializer, NotAdminUsersSerializer,
                             TitleSerializer, SignUpSerializer, GetTokenSerializer, ReviewSerializer, CommentSerializer)




class APIGetToken(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        confirmation_code = data['confirmation_code']
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return Response(
                {'username': 'Пользователь не найден!'},
                status=status.HTTP_404_NOT_FOUND)

        if default_token_generator.check_token(user, confirmation_code):
            token = AccessToken.for_user(user)
            return Response({'token': str(token)},
                            status=status.HTTP_201_CREATED)
        return Response(
            {'confirmation_code': 'Неверный код подтверждения!'},
            status=status.HTTP_400_BAD_REQUEST)


class APISignup(APIView):

    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=[data['to_email']]
        )
        email.send()

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        key = default_token_generator.make_token(user)

        email_body = (
            f'\nКод подтверждения: {key}'
        )
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'Код подтверждения для доступа к API!'
        }
        self.send_email(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUsersSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    lookup_field = 'username'
    filter_backends = (SearchFilter, )
    search_fields = ('username', )


    @action(methods=['GET', 'PATCH'], detail=False, permission_classes=(permissions.IsAuthenticated,), url_path='me')
    def get_current_user_info(self, request):
        serializer = AdminUsersSerializer(request.user)
        if request.method == 'PATCH':
            if request.user.role == 'admin':
                serializer = AdminUsersSerializer(
                    request.user,
                    data=request.data,
                    partial=True)
            else:
                serializer = NotAdminUsersSerializer(
                    request.user,
                    data=request.data,
                    partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data)

class GenreViewSet(viewsets.ModelViewSet):
    quereset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', )


class CategoryViewSet(viewsets.ModelViewSet):
    quereset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', )


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, )


class ReviewViewSet(viewsets.ModelViewSet):
    """View представления оценок."""
    serializer_class = ReviewSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get_title(self):
        return get_object_or_404(Title, id=self.kwargs.get("title_id"))

    def receive_queryset(self):
        return self.get_title().reviews.all()

    def execute_generate(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentViewSet(viewsets.ModelViewSet):
    """View представления комментариев."""
    serializer_class = CommentSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get_review(self):
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def receive_queryset(self):
        return self.get_review().comments.all()

    def execute_generate(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())