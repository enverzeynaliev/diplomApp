# Generated by Django 4.0.4 on 2022-05-28 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='departments',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='departments',
            name='path',
            field=models.CharField(max_length=100),
        ),
    ]
