# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uwhapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_donation', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uwhapp.DonorHistory')),
            ],
        ),
        migrations.CreateModel(
            name='RequestToDonor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_units', models.IntegerField()),
                ('blood_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uwhapp.BloodBank')),
            ],
        ),
        migrations.RemoveField(
            model_name='requests',
            name='blood_bank',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='last_donation',
        ),
        migrations.DeleteModel(
            name='Requests',
        ),
        migrations.AddField(
            model_name='requesttodonor',
            name='requestee_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uwhapp.Donor'),
        ),
        migrations.AddField(
            model_name='donorhistory',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uwhapp.Donor'),
        ),
    ]
