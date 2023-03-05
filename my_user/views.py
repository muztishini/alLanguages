from rest_framework import status
from rest_framework.response import Response
# from lottee_new.helpers import get_object_or_none
from my_user.serializers import UserSerializer, UpdatePasswordSerializer, ResetPasswordSerializer
from my_user.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes

from rest_framework.views import APIView
from rest_framework.response import Response


'''@api_view(['PATCH'])
def reset_password(request):
    user = get_object_or_none(User, identifier=request.data['identifier'])
    if user:
        serializer = ResetPasswordSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_412_PRECONDITION_FAILED)'''


class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = get_user_model()
    serializer_class = UserSerializer


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(
            status=status.HTTP_200_OK,
            data={'user': serializer.data}
        )

    def partial_update(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            instance=request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class UpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UpdateNativeView(APIView):
    def patch(self, request):
        user = User.objects.get(id=request.user.id)
        user.native_id = request.data['id']
        user.save(update_fields=['native_id'])

        return Response()


class UpdateLearnView(APIView):
    def patch(self, request):
        user = User.objects.get(id=request.user.id)
        user.learn_id = request.data['id']
        user.save(update_fields=['learn_id'])

        return Response()
