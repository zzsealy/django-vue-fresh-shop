from datetime import datetime

from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey

from shop.apps.utils import get_model
# Create your models here.
User = get_user_model()
Goods = get_model('goods', 'Goods')


class UserFav(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    '''
    用户留言
    '''

    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, '投诉'),
        (3, '咨询'),
        (4, '售后'),
        (5, '求购'),
    )

    user = models.ForeignKey(User, verbose_name="用户", on_delete=CASCADE)
    msg_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                   help_text='留言类型:1(留言), 2(投诉), 3(询问), 4(售后), 5(求购)')
    subject = models.CharField(max_length=100, default='', verbose_name="主题")
    message = models.TextField(
        default='',  verbose_name='留言内容', help_text='留言内容')
    file = models.FileField(verbose_name='上传的文件', help_text='上传的文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s: %s" % (self.user.name, self.subject)


class UserAddress(models.Model):
    '''
    用户收获地址
    '''
    user = models.ForeignKey(User, on_delete=CASCADE)
    
