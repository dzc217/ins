# Generated by Django 3.2.9 on 2021-11-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortpath',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='服务器路径'),
        ),
    ]