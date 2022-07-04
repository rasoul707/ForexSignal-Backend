from lib2to3.pgen2 import token
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Account
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from upload.serializers import ImageSerializer
from license.serializers import LicenseSerializerAccount
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.base import AuthProcess
from allauth.utils import email_address_exists, get_username_max_length


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
            'avatar',
            'broker',
            'token',
            'referrals',
            'inviter',
            'license',
            'license_expire',
        ]


class CustomRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED,
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def custom_signup(self, request, user):
        inviter_account = Account.objects.get(token=request.data['ref'])
        print(inviter_account)

        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
