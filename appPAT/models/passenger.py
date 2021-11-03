from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError('El usuario debe tener un email')
        user = self.model(email=email)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Passenger(AbstractBaseUser, PermissionsMixin):

    id_passenger = models.BigAutoField(primary_key=True)
    name = models.CharField('Name', max_length=100)
    document = models.CharField('Document', max_length=20, unique=True)
    email = models.EmailField('Email', max_length=70, unique=True)
    password = models.CharField('Password', max_length=256)
    birth_date = models.DateTimeField('Birth Date', null=True)
    cellphone = models.CharField('Phone Number', max_length=20)
    gender_list = [('F', 'Femenino'), ('M', 'Masculino')]
    gender = models.CharField(
        'Gender', max_length=1,
        choices=gender_list, default='F'
    )

    def save(self, **kwargs):
        something = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, something)
        super().save(**kwargs)

    class Meta:
        db_table = "passenger"
        verbose_name = "Passenger"
        verbose_name_plural = "Passengers"
        ordering = ["id_passenger"]

    objects = UserManager()
    USERNAME_FIELD = 'email'
    USER_ID_FIELD = 'id_passenger'
