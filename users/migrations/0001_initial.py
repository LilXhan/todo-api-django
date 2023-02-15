# Generated by Django 4.1.6 on 2023-02-14 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('realname', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
