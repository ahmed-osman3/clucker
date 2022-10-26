from unittest.util import _MAX_LENGTH
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        max_length=30,
         unique=True,
         validators=[RegexValidator(
            regex = r'^@\w{3,}$', # ^ = circumflex symbol. corresponds to beginning of string. $ = ending of string. 
            message = 'Username must consist of @ followed by at least three alphanumericals'
         )]
    )
    first_name = models.CharField(
        blank = False,
        unique = False,
        max_length = 50
    )
    last_name = models.CharField(
        blank = False,
        unique = False,
        max_length = 50
    )
    email = models.EmailField(
        unique = True,
        validators = [RegexValidator(
            regex = r'^\w{1,}@\w{1,}.\w{1,}$'
        )]
    )
    bio = models.TextField(
        blank = True,
        unique = False,
        max_length = 520
    )




class Post(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE),
    text = models.CharField(
        max_length = 280,
    ),
    created_at = models.DateTimeField(
        auto_now_add = True,
        editable = False,
    )

    class Meta:
        ordering = ["-created_at"],
        verbose_name_plural = "posts"
