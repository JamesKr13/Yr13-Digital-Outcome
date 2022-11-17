from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


    
class UserManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username: 
            raise ValueError('Users must have an username')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractBaseUser):
    club = models.ForeignKey("Club.Clubs",verbose_name=('Club'),null=True,blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pics')
    username = models.CharField(unique=True,max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):
        print(self.username)
        print(type(self.username))
        return str(self.username)
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
