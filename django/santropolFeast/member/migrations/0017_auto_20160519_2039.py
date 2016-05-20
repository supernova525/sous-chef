# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-19 20:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0016_auto_20160519_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='billing_payment_type',
            field=models.CharField(choices=[('', 'Payment type'), ('check', 'Check'), ('cash', 'Cash'), ('debit', 'Debit card'), ('credit', 'Credit card'), ('eft', 'EFT')], max_length=10, null=True, verbose_name='Payment Type'),
        ),
        migrations.AddField(
            model_name='client',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French')], default='fr', max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=6, verbose_name='postal code'),
        ),
        migrations.AlterField(
            model_name='client',
            name='alert',
            field=models.TextField(blank=True, null=True, verbose_name='alert client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Address', verbose_name='billing address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='emergency_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact', to='member.Member', verbose_name='emergency contact'),
        ),
        migrations.AlterField(
            model_name='client',
            name='facturation',
            field=models.CharField(choices=[('default', 'Default'), ('low income', 'Low income'), ('solidary', 'Solidary')], default='default', max_length=10, verbose_name='facturation type'),
        ),
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('D', 'Pending'), ('A', 'Active'), ('S', 'Paused'), ('N', 'Stop: no contact'), ('C', 'Stop: contact'), ('I', 'Deceased')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('Home phone', 'Home phone'), ('Cell phone', 'Cell phone'), ('Work phone', 'Work phone'), ('Email', 'Email')], max_length=100, verbose_name='contact type'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank='True', choices=[('', 'Gender'), ('F', 'Female'), ('M', 'Male')], default='U', max_length=1, null='True'),
        ),
        migrations.AlterField(
            model_name='note',
            name='creation_date',
            field=models.DateField(auto_now_add=True, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='note',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='is read'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(verbose_name='text note'),
        ),
        migrations.AlterField(
            model_name='referencing',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 19), verbose_name='Referral date'),
        ),
        migrations.AlterField(
            model_name='referencing',
            name='referral_reason',
            field=models.TextField(verbose_name='Referral reason'),
        ),
    ]
