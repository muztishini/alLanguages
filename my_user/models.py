from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# from alLanguages.settings import EMAIL_HOST_USER
from my_user.manager import UserManager
from language.models import Language


class User(AbstractUser):
    """ User model """
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, null=False)

    # user languages
    native = models.ForeignKey(Language, related_name='native', on_delete=models.CASCADE, null=True)
    learn = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    balance = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
    energy = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email or ''
