# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class CurrnetMenuList(models.Model):
    users_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USERS_user_id', primary_key=True)  # Field name made lowercase.
    current_menu = models.ForeignKey('Menu', models.DO_NOTHING, db_column='current_menu')

    class Meta:
        managed = False
        db_table = 'currnet_menu_list'
        unique_together = (('users_user', 'current_menu'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Ingredients(models.Model):
    menu_menu_name = models.ForeignKey('Menu', models.DO_NOTHING, db_column='MENU_menu_name', primary_key=True)  # Field name made lowercase.
    ingredient = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Market(models.Model):
    market_url = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'market'


class Menu(models.Model):
    menu_name = models.CharField(primary_key=True, max_length=45)
    how_make = models.CharField(max_length=15, blank=True, null=True)
    sort = models.CharField(max_length=15, blank=True, null=True)
    calorie = models.IntegerField(blank=True, null=True)
    carbohydrate = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    salt = models.IntegerField(blank=True, null=True)
    big_image = models.CharField(db_column='big_Image', max_length=100, blank=True, null=True)  # Field name made lowercase.
    small_image = models.CharField(db_column='small_Image', max_length=100, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class MenuRecipe(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    recipe_image = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_recipe'


class MyappFood(models.Model):
    food_name = models.CharField(db_column='Food_name', max_length=30)  # Field name made lowercase.
    ingredient1 = models.CharField(max_length=30)
    ingredient2 = models.CharField(max_length=30)
    ingredient3 = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'myapp_food'


class Recipe(models.Model):
    menu_menu_name = models.ForeignKey(Menu, models.DO_NOTHING, db_column='MENU_menu_name', primary_key=True)  # Field name made lowercase.
    sequence = models.CharField(max_length=100, blank=True, null=True)
    recipe_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class TakePicIngredients(models.Model):
    current_ingredients = models.CharField(max_length=45, blank=True, null=True)
    users_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USERS_user_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'take_pic_ingredients'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
