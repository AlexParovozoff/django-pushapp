# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pushapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pushapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='device_id',
            field=models.UUIDField(help_text='UDID / UIDevice.identifierForVendor()', verbose_name='Device ID', blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='gcmdevice',
            name='device_id',
            field=pushapp.fields.HexIntegerField(help_text='ANDROID_ID / TelephonyManager.getDeviceId() (always as hex)', db_index=True, verbose_name='Device ID', blank=True, null=True),
        ),
    ]
