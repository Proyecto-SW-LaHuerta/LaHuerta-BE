# Generated by Django 3.2.7 on 2022-03-03 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_rename_id_user_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=254),
        ),
    ]
