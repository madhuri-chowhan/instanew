# Generated by Django 4.0.4 on 2022-09-06 13:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='likePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('post_id', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(blank=True, default='static/user.png', null=True, upload_to='dp_images/%y/%m/%d')),
                ('bio', models.TextField(blank=True, null=True)),
                ('joined_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Display', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user_post', models.ImageField(upload_to='post_image/%y/%m/%d')),
                ('caption', models.TextField(blank=True, null=True)),
                ('posted_at', models.DateTimeField(default=datetime.datetime.now)),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_follower', to='account.userinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_followed', to='account.userinfo')),
            ],
        ),
    ]
