# Generated by Django 3.2.8 on 2021-10-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]