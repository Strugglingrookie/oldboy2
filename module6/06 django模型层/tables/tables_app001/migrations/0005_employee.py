# Generated by Django 2.2.3 on 2019-08-11 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables_app001', '0004_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('age', models.BigIntegerField()),
                ('sal', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dep', models.CharField(max_length=32)),
            ],
        ),
    ]
