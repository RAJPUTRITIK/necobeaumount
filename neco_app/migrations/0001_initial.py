# Generated by Django 4.2.4 on 2023-08-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveIntegerField()),
                ('owner_name', models.CharField(max_length=50)),
                ('member', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=11)),
            ],
        ),
    ]
