# Generated by Django 3.2.7 on 2022-03-09 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_auto_20220308_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categoryType',
            field=models.CharField(choices=[('N', 'Nacional'), ('I', 'Importado'), ('V', 'Verduras_Hortalizas')], max_length=30),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='payType',
            field=models.CharField(choices=[('E', 'Efectivo'), ('T', 'Tarjeta')], max_length=15),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='userType',
            field=models.CharField(choices=[('A', 'Administrador'), ('N', 'Natural')], max_length=15),
        ),
    ]