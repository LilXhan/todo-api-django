# Generated by Django 4.1.6 on 2023-02-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersjwt', '0004_remove_jwtuser_date_of_birth_jwtuser_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jwtuser',
            name='email',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
