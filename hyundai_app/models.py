# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from numpy import arange
import numpy as np

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class FinalTrainDf(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    marka = models.BigIntegerField(blank=True, null=True)
    model = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    engine = models.FloatField(blank=True, null=True)
    gearbox = models.BigIntegerField(blank=True, null=True)
    transmission = models.BigIntegerField(blank=True, null=True)
    ban_type = models.BigIntegerField(blank=True, null=True)
    fuel_type = models.BigIntegerField(blank=True, null=True)
    color = models.BigIntegerField(blank=True, null=True)
    used_by_km = models.BigIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_train_df'

class Prediction1(models.Model):

    MARKA_CHOICES = (
        (1,'Hyundai'),
        (9,'Chevrolet')

    )

    MODEL_CHOICES = (
        (11,'Cruze'),
        (29,'Elantra'),
        (38,'Accent')
        
    )

    YEAR_CHOICES = [(i,i) for i in range(1980,2022)]

    ENGINE_CHOICES = (
        (0.5,0.5),
        (0.6,0.6),
        (0.7,0.7),
        (0.8,0.8),
        (0.9,0.9),
        (1.0,1.0),
        (1.1,1.1),
        (1.2,1.2),
        (1.3,1.3),
        (1.4,1.4),
        (1.5,1.5),
        (1.6,1.6),
        (1.7,1.7),
        (1.8,1.8),
        (1.9,1.9),
        (2.0,2.0),
        (2.1,2.1),
        (2.2,2.2),
        (2.3,2.3),
        (2.4,2.4),
        (2.5,2.5),
        (2.6,2.6),
        (2.7,2.7),
        (2.8,2.8),
        (2.9,2.9),
        (3.0,3.0),
        (3.1,3.1),
        (3.2,3.2),
        (3.3,3.3),
        (3.4,3.4),
        (3.5,3.5),
        (3.6,3.6),
        (3.7,3.7),
        (3.8,3.8),
        (3.9,3.9),
        (4.0,4.0),
        (4.1,4.1),
        (4.2,4.2),
        (4.3,4.3),
        (4.4,4.4),
        (4.5,4.5),
        (4.6,4.6),
        (4.7,4.7),
        (4.8,4.8),
        (4.9,4.9),
        (5.0,5.0),
        (5.1,5.1),
        (5.2,5.2),
        (5.3,5.3),
        (5.4,5.4),
        (5.5,5.5),
        (5.6,5.6),
        (5.7,5.7),
        (5.8,5.8),
        (5.9,5.9),
        (6.0,6.0)
    
    )


    GEARBOX_CHOICES = (
        (1,'AVTOMAT'),
        (2,'MEXANIKI'),
        (3,'VARIATOR'),
        (4,'ROBOTLAŞDIRILMIŞ')
    )

    TRANSMISSION_CHOICES = (
        (1,'ÖN'),
        (2,'TAM'),
        (3,'ARXA')
    )
    BAN_CHOICES = (
        (1,'SEDAN'),
        (2,'OFFROADER / SUV'),
        (3,'UNIVERSAL'),
        (4,'HETÇBEK / LIFTBEK'),
        (5,'VAN'),
        (6,'KUPE'),
        (7,'FURQON'),
        (8,'MINIVAN'),
        (9,'KABRIO'),
        (10,'MIKROAVTOBUS'),
        (11,'PIKAP'),
        (12,'YÜK MAŞINI'),
        (13,'AVTOBUS'),
        (14,'MOTOSIKLET'),
        (15,'DARTQI'),
        (16,'RODSTER'),
        (17,'QOLFKAR')
    )
    FUEL_CHOICES = (
        (1,'BENZIN'),
        (2,'DIZEL'),
        (3,'HIBRID'),
        (4,'ELEKTRO'),
        (5,'QAZ')
    )
    COLOR_CHOICES = (
        (1,'YAŞ ASFALT'),
        (2,'AĞ'),
        (3,'BOZ'),
        (4,'GÖY'),
        (5,'QARA'),
        (6,'SARI'),
        (7,'GÜMÜŞÜ'),
        (8,'QƏHVƏYI'),
        (9,'MAVI'),
        (10,'YAŞIL'),
        (11,'TÜND QIRMIZI'),
        (12,'QIZILI'),
        (13,'BEJ'),
        (14,'QIRMIZI'),
        (15,'NARINCI'),
        (16,'BƏNÖVŞƏYI'),
        (17,'ÇƏHRAYI')
    )


    id = models.AutoField(primary_key=True)
    marka= models.IntegerField(null=True,choices = MARKA_CHOICES)
    model= models.IntegerField(null=True,choices = MODEL_CHOICES)
    year= models.IntegerField(null=True,choices = YEAR_CHOICES)
    engine = models.FloatField(null=True,choices = ENGINE_CHOICES)
    gearbox =  models.IntegerField(null=True,choices = GEARBOX_CHOICES)
    transmission =  models.IntegerField(null=True,choices = TRANSMISSION_CHOICES)
    ban_type = models.IntegerField(null=True,choices = BAN_CHOICES)
    fuel_type = models.IntegerField(null=True,choices = FUEL_CHOICES)
    color = models.IntegerField(null=True,choices = COLOR_CHOICES)
    used_by_km = models.IntegerField(default=0)
    predicted_price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.marka