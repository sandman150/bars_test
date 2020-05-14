# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-13 14:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('app', '0003_remove_permissions_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissions',
            name='codename',
        ),
        migrations.RemoveField(
            model_name='permissions',
            name='name',
        ),
        migrations.AddField(
            model_name='permissions',
            name='permission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Permission', verbose_name='permission'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contenttypes',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content_type'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]