from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Account
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from upload.serializers import ImageSerializer
from license.serializers import LicenseSerializerAccount
from allauth.account.adapter import get_adapter


class CustomUserDetailSerializer(UserDetailsSerializer):

    avatar = ImageSerializer(read_only=True)
    license = LicenseSerializerAccount(read_only=True)

    class Meta():
        model = Account
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_verified_email',
            'avatar',
            'broker',
            'token',
            'referrals',
            'inviter',
            'license',
            'license_expire',
        ]


class CustomRegisterSerializer(serializers.ModelSerializer):

    # print("hmmmmm")
    first_name = serializers.CharField(required=True)

    class Meta():
        model = Account
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_verified_email',
            'avatar',
            'broker',
            'token',
            'referrals',
            'inviter',
            'license',
            'license_expire',
        ]

    def save(self, request):
        print("Hiiii")
        adapter = get_adapter()
        user = adapter.new_user(request)

        # self.cleaned_data = self.get_cleaned_data()
        # user = adapter.save_user(request, user, self, commit=False)
        # if "password1" in self.cleaned_data:
        #     try:
        #         adapter.clean_password(
        #             self.cleaned_data['password1'], user=user)
        #     except DjangoValidationError as exc:
        #         raise serializers.ValidationError(
        #             detail=serializers.as_serializer_error(exc)
        #         )
        # user.save()
        # self.custom_signup(request, user)
        # setup_user_email(request, user, [])
        return user


# class RegisterSerializer(UserDetailsSerializer):
#     email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
#     first_name = serializers.CharField(required=True, write_only=True)
#     last_name = serializers.CharField(required=True, write_only=True)
#     password1 = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)

#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_settings.UNIQUE_EMAIL:
#             if email and email_address_exists(email):
#                 raise serializers.ValidationError(
#                     "A user is already registered with this e-mail address."
#                 )
#         return email

#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)

#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(
#                 "The two password fields didn't match."
#             )
#         return data

#     def get_cleaned_data(self):
#         return {
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#         }

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         setup_user_email(request, user, [])
#         user.save()
#         return user
