from django.db import models


# Create your models here.

class User(models.Model):
    """User模型"""
    GENDERS = (
        ('male', '男'),
        ('female', '女'),
    )
    
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=20, db_index=True, verbose_name='昵称')
    gender = models.CharField(max_length=16, choices=GENDERS, verbose_name='性别')
    birthday = models.DateField(default='2000-01-01', verbose_name='出生日期')
    icon = models.ImageField(verbose_name='头像', default='default.jpg')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=16, verbose_name='所在城市')
    
    class Meta:
        db_table = 'user'
