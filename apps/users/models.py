from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from utils.send_email.send_email import send_email_verify,sign_value
from utils.validates.validates import validate_digits,validate_alnum,validate_letters_and_spaces,validate_letters_numbers_and_spaces

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self.db)
        # process send email verify
        # token = sign_value(user.id)
        # path = f"/accounts/verify/?token={token}"
        # send_email_verify(user.email,path,token)
        return user
    
    def create_user(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, False , False ,**extra_fields)
    
    def create_superuser(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, True , True ,**extra_fields)
    



class User(AbstractBaseUser, PermissionsMixin):   
        
    
    USER_TYPE_CHOICES = (
        ('chef', 'chef'),
        ('waiter', 'waiter'),
        ('barman', 'barman'),
        ('economic', 'economic'),
        ('administrator', 'administrator'),
      
        # Add other user types here
    )

    user_type = models.CharField(max_length=13, choices=USER_TYPE_CHOICES, default='waiter') 
    username = models.CharField(validators=[MinLengthValidator(3),validate_alnum],max_length=50, unique=True,blank = False, null= False)
    email = models.EmailField( max_length=50 , unique=True, blank = False, null= False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    movil =models.CharField(validators=[MinLengthValidator(8),validate_digits], max_length=8, blank = False, null= False)
    verified_email = models.BooleanField('Verify email',default=True)
    objects = UserManager()
    name = models.CharField( max_length=50,validators=[MinLengthValidator(3),validate_letters_and_spaces],blank=False, null=False)
    last_name = models.CharField(validators=[MinLengthValidator(3),validate_letters_and_spaces], max_length=50, blank=False, null=False)
    ci=models.CharField(validators=[MinLengthValidator(11),validate_digits], max_length=11, unique=False ,blank = False, null= False)
    
    class Meta:   
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'movil','name','last_name','ci',]
    
    def natural_key(self):
        return (self.username)
    
    def __str__(self) -> str:
        return f'{self.username}'