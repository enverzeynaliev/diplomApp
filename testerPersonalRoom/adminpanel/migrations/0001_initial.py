# Generated by Django 4.0.4 on 2022-05-28 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('descriptionformat', models.IntegerField()),
                ('parent', models.IntegerField()),
                ('sortorder', models.IntegerField()),
                ('coursecount', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('path', models.CharField(max_length=50)),
            ],
        ),
    ]
