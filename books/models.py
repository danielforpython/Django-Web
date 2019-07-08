from django.db import models

# Create your models here.
from django.db import models


class BookInfoManager(models.Manager):
    def all(self):
        return super().filter(isDelete=True)

# 定义图书模型类BookInfo
class BookInfo(models.Model):
    # 指定btitle对应的字段名为title
    btitle = models.CharField(max_length=20, db_column='title')

    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    class Meta:
        verbose_name_plural='图书模型类'
        verbose_name='图书列表'
        ordering=['bpub_date',]

# 新闻类型
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)  # 新闻类别

# 新闻
class NewsInfo(models.Model):
    ntitle = models.CharField(max_length=60)  # 新闻标题
    ncontent = models.TextField()  # 新闻内容
    npub_date = models.DateTimeField(auto_now_add=True)  # 新闻发布时间

    # 通过ManyToManyField建立TypeInfo类和NewsInfo类之间多对多的关系
    typeinfo= models.ManyToManyField('TypeInfo')  #关系表

    class Meta:
        verbose_name_plural='新闻模型类'
        verbose_name = '新闻'





# 定义人物模型类PersonInfo
class PersonInfo(models.Model):
    pname = models.CharField(max_length=20)  # 人物姓名
    pgender = models.BooleanField(default=True)  # 人物性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    fbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    # 人物描述，数据库中的字段可以为空，但后台管理页面的输入框不能为空
    pcomment = models.CharField(max_length=200, null=True, blank=False)

    class Meta:
        verbose_name_plural = '人物模型类'
        verbose_name = '人物列表'
        ordering = ['id',]


# 定义地区模型类AreaInfo，存储省、市、区县信息


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)  # 地区名称

    # 上级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "地区模型类"
        verbose_name = '地区模型类'

