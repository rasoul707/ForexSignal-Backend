from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class Account(AbstractUser):

    is_staff = models.BooleanField(
        "staff",
        default=False,
        help_text="Can log into administration",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="User activation",
    )
    is_superuser = models.BooleanField(
        "superuser",
        default=False,
        help_text="Have all permissions",
    )
    first_name = models.CharField(
        "first name", max_length=150, blank=False, null=False,
    )
    last_name = models.CharField(
        "last name", max_length=150, blank=False, null=False,
    )
    email = models.EmailField(
        "email address", blank=False, null=False, unique=True,
    )
    avatar = models.ForeignKey(
        "upload.Image", on_delete=models.SET_NULL, blank=True, null=True
    )
    broker = models.ForeignKey(
        "notice.Broker", on_delete=models.SET_NULL, blank=True, null=True
    )
    token = models.CharField(
        max_length=20, default=get_random_string(length=16),
    )
    referrals = models.ManyToManyField(
        "authentication.Account", related_name='referrals_accounts', blank=True,
    )
    inviter = models.ForeignKey(
        "authentication.Account", on_delete=models.SET_NULL, blank=True, null=True, related_name='inviter_account'
    )
    license = models.ForeignKey(
        "license.License", on_delete=models.SET_NULL, blank=True, null=True
    )
    license_expire = models.DateTimeField(
        "license_expire", default=timezone.now
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    # first_name
    # last_name
    # email
    # username
    # license
    # license_expire
    # inviter
    # password
