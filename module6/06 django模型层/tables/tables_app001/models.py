from django.db import models

# Create your models here.


class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    # 一对一  与AuthorDetail
    authorDetail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.BigIntegerField()
    addr = models.CharField(max_length=32)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.age


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    read_num = models.BigIntegerField(default=0)
    comment_num = models.BigIntegerField(default=0)

    # 一对多
    publish = models.ForeignKey(to='Publish', to_field='id', on_delete=models.CASCADE)

    # 多对多    自动创建第三张表  book_authors
    authors = models.ManyToManyField(to='Author',)

    def __str__(self):
        return self.title


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    age = models.BigIntegerField()
    sal = models.DecimalField(max_digits=5, decimal_places=1)
    dep = models.CharField(max_length=32)

    def __str__(self):
        return self.title


