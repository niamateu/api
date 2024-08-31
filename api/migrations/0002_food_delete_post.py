# Generated by Django 5.1 on 2024-08-17 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='品物')),
                ('date', models.CharField(max_length=255, verbose_name='消費期限')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='数量')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
