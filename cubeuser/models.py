from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Cubeuser(AbstractUser):
    SEX_MAN = 1
    SEX_WOMAN = 2
    SEX_UNKNOW = 0
    SEX_ITEMS = (
        (SEX_MAN, '男'),
        (SEX_WOMAN, '女'),
        (SEX_UNKNOW, '未知'),
    )
    sex = models.PositiveIntegerField(default=SEX_UNKNOW, choices=SEX_ITEMS, verbose_name='性别')
    truename = models.CharField(max_length=10, default='未知', verbose_name='真实姓名')
    idnum = models.CharField(max_length=20, default='未知', verbose_name='身份证号码')
    emergencyname = models.CharField(max_length=10, default='未知', verbose_name='紧急联络人姓名')
    emergencyphone = models.CharField(max_length=20, default='未知', verbose_name='紧急联络人电话')
    picture = models.ImageField(upload_to="IDimg/", null=True, blank=True)
    birthday = models.DateField(verbose_name='出生日期', null=True, blank=True)
    #area
    address = models.CharField(max_length=100, default='未知', verbose_name='邮寄地址')
    #organization

    class Meta:
        verbose_name = verbose_name_plural = '魔方用户'