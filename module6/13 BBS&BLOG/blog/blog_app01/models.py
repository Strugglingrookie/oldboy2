from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    # 用户信息
    nid = models.AutoField(primary_key=True)
    phone_num = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to='avatars/', default='avatars/default.png')
    create_time = models.DateField(verbose_name='创建时间', auto_now_add=True)

    blog = models.OneToOneField(to='UserBlog', to_field='nid', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class UserBlog(models.Model):
    # 博客站点信息
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, verbose_name='个人博客标题')
    site_name = models.CharField(max_length=64, verbose_name='站点名称')
    theme = models.CharField(max_length=64, verbose_name='博客主题')

    def __str__(self):
        return self.title


class Category(models.Model):
    # 博客个人文章分类
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='分类标题')
    blog = models.ForeignKey(verbose_name='所属博客', to='UserBlog', to_field='nid', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(models.Model):
    # 博客文章标签
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='标签名称')
    blog = models.ForeignKey(verbose_name='所属博客', to='UserBlog', to_field='nid', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Article(models.Model):
    # 博客文章
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述')
    create_time = models.DateField(verbose_name='创建时间', auto_now_add=True)

    comment_cnt = models.IntegerField(default=0, verbose_name='评论数')
    up_cnt = models.IntegerField(default=0, verbose_name='点赞数')
    down_cnt = models.IntegerField(default=0, verbose_name='踩灰数')

    user = models.ForeignKey(to='UserInfo', to_field='nid', verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', to_field='nid', verbose_name='分类', null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tag', through='Article2Tag', through_fields=('article', 'tag'))

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    # 博客文章和标签的关系表
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='文章', to='Article', to_field='nid', on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to='Tag', to_field='nid', on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ('article', 'tag'),
        ]

    def __str__(self):
        v = self.article.title + '----' + self.tag.title
        return v


class ArticleUpDown(models.Model):
    # 文章点赞踩灰表
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='UserInfo', to_field='nid', null=True, on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', to_field='nid', null=True, on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = [
            ('article', 'user'),
        ]


class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid', null=True, on_delete=models.CASCADE)
    article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='nid', null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, verbose_name='评论内容')
    create_time = models.DateField(verbose_name='创建时间', auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
