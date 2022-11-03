from django.conf import settings
from  django.db import  models
from  django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.contrib.auth import get_user_model
#
# user = get_user_model()

# Create your models here.
class  useraccountManager(BaseUserManager):
            def create_user(self, email, name, password=None):
                    if not  email:
                              raise ValueError('Users must have a Email address')
                    email = self.normalize_email(email) 
                    User = self.model(email=email, name=name)
                    User.set_password(password)
                    User.save()
                    return User

            def create_superuser(self, email, name, password=None):
                    if not  email:
                              raise ValueError('Users must have a Email address')
                    email = self.normalize_email(email) 
                    User = self.model(email=email, name=name, is_superuser=True)
                    User.set_password(password)
                    User.save()
                    return User

class  useraccount(AbstractBaseUser, PermissionsMixin):
          email = models.EmailField(max_length=300, unique=True)
          name = models.CharField(max_length=250, verbose_name='name')
          username = models.CharField(max_length=250, null=True, blank=True)
          followers = models.ManyToManyField(settings.AUTH_USER_MODEL)
          is_active = models.BooleanField(default=False)
          is_staff = models.BooleanField(default=False)
          is_superuser = models.BooleanField(default=False)
          objects = useraccountManager()

          USERNAME_FIELD = 'email'
          REQUIRED_FIELDS = ['name']
          
          def get_full_name(self):
                    return self.name

          def get_short_name(self):
                    return self.name
          
          def __str__(self):
                    return self.username