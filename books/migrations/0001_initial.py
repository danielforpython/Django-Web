# Generated by Django 2.2.2 on 2019-06-18 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(db_column='title', max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '图书列表',
                'verbose_name_plural': '图书',
                'ordering': ['bpub_date'],
            },
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('pgender', models.BooleanField(default=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('pcomment', models.CharField(max_length=200, null=True)),
                ('fbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookInfo')),
            ],
            options={
                'verbose_name': '人物列表',
                'verbose_name_plural': '人物',
                'ordering': ['id'],
            },
        ),
    ]
