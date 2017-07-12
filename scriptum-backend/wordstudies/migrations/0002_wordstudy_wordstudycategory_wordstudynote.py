# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-12 04:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wordstudies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_studies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WordStudyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='wordstudies.WordStudy')),
            ],
        ),
        migrations.CreateModel(
            name='WordStudyNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='wordstudies.WordStudyCategory')),
                ('verse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='wordstudies.Verse')),
            ],
        ),
    ]