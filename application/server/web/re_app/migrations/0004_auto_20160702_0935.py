# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('re_app', '0003_auto_20160701_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'managed': True, 'verbose_name': '\u0413\u043e\u0440\u043e\u0434', 'verbose_name_plural': '\u0433\u043e\u0440\u043e\u0434\u0430'},
        ),
        migrations.AlterModelOptions(
            name='station',
            options={'managed': True, 'verbose_name': '\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0443\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043e\u0442\u0445\u043e\u0434\u043e\u0432', 'verbose_name_plural': 'c\u0442\u0430\u043d\u0446\u0438\u0438 \u0443\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'managed': True, 'verbose_name': '\u0423\u043b\u0438\u0446\u0430', 'verbose_name_plural': '\u0443\u043b\u0438\u0446\u044b'},
        ),
        migrations.AlterModelOptions(
            name='trash',
            options={'managed': True, 'verbose_name': '\u0423\u0442\u0438\u043b\u044c', 'verbose_name_plural': '\u0443\u0442\u0438\u043b\u044c'},
        ),
        migrations.AlterModelOptions(
            name='trashclass',
            options={'managed': True, 'verbose_name': '\u041a\u043b\u0430\u0441\u0441 \u043e\u0442\u0445\u043e\u0434\u043e\u0432', 'verbose_name_plural': '\u043a\u043b\u0430\u0441\u0441\u044b \u043e\u0442\u0445\u043e\u0434\u043e\u0432'},
        ),
        migrations.AlterModelOptions(
            name='trashstation',
            options={'managed': True, 'verbose_name': '\u0423\u0442\u0438\u043b\u044c-\u0421\u0442\u0430\u043d\u0446\u0438\u044f', 'verbose_name_plural': '\u0443\u0442\u0438\u043b\u044c-\u0421\u0442\u0430\u043d\u0446\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='trashtype',
            options={'managed': True, 'verbose_name': '\u0422\u0438\u043f \u043e\u0442\u0445\u043e\u0434\u043e\u0432', 'verbose_name_plural': '\u0442\u0438\u043f\u044b \u043e\u0442\u0445\u043e\u0434\u043e\u0432'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', 'verbose_name_plural': '\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438'},
        ),
        migrations.AlterModelOptions(
            name='usertrash',
            options={'managed': True, 'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c-\u0423\u0442\u0438\u043b\u044c', 'verbose_name_plural': '\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c-\u0423\u0442\u0438\u043b\u044c'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
        migrations.AlterField(
            model_name='station',
            name='add_date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='station',
            name='building',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u0440\u043f\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='station',
            name='house',
            field=models.SmallIntegerField(verbose_name='\u0414\u043e\u043c'),
        ),
        migrations.AlterField(
            model_name='station',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u0421\u0442\u0430\u043d\u0446\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='station',
            name='position_x',
            field=models.FloatField(blank=True, null=True, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='station',
            name='position_y',
            field=models.FloatField(blank=True, null=True, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='station',
            name='raiting',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='\u041f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='station',
            name='show',
            field=models.BooleanField(default=False, verbose_name='\u0412\u0438\u0434\u043d\u0430 \u043d\u0430 \u043a\u0430\u0440\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='station',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.Street', verbose_name=b'\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='station',
            name='update_date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='street',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.City', verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u0423\u043b\u0438\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='trash',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.TrashClass', verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='trash',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='trash',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.TrashType', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf'),
        ),
        migrations.AlterField(
            model_name='trashclass',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='trashclass',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u041a\u043b\u0430\u0441\u0441 \u043e\u0442\u0445\u043e\u0434\u043e\u0432'),
        ),
        migrations.AlterField(
            model_name='trashstation',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.Station', verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd0\xbd\xd1\x86\xd0\xb8\xd1\x8f \xd1\x83\xd1\x82\xd0\xb8\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='trashstation',
            name='trash_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.TrashType', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xbe\xd1\x82\xd1\x85\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2'),
        ),
        migrations.AlterField(
            model_name='trashtype',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='trashtype',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='\u0422\u0438\u043f'),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=30, unique=True, verbose_name='\u041b\u043e\u0433\u0438\u043d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.BigIntegerField(unique=True, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='user',
            name='raiting',
            field=models.IntegerField(verbose_name='\u0423\u0440\u043e\u0432\u0435\u043d\u044c'),
        ),
        migrations.AlterField(
            model_name='user',
            name='reg_date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='usertrash',
            name='trash',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.Trash', verbose_name='\u0423\u0442\u0438\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='usertrash',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_app.User', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]
