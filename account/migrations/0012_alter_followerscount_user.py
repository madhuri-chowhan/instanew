# Generated by Django 4.0.4 on 2022-07-27 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_followerscount_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerscount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userinfo'),
        ),
    ]