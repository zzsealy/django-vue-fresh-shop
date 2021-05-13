from email.policy import default
from random import choice
from datetime import datetime
from tabnanny import verbose
from django.db import models

# Create your models here.

class GoodsCategory(models.Model):
    """
    产品类 自引用
    """

    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=20, verbose_name="类名code", help_text="类名code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录", on_delete=models.CASCADE,
                                        related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name
    

    def __str__(self) -> str:
        return self.name

class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brand/images") # ImageField 在数据库中存储的时候是个Char
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name

class Goods(models.Model):
    """
    商品
    """
    pass

