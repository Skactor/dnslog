# Generated by Django 3.1.1 on 2020-09-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_dnslog_client_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblog',
            name='method',
            field=models.CharField(default='GET', help_text='请求方法', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weblog',
            name='body',
            field=models.TextField(blank=True, help_text='请求体'),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='header',
            field=models.TextField(help_text='请求头', verbose_name='header'),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='ip',
            field=models.GenericIPAddressField(help_text='客户端地址', verbose_name='remote_addr'),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='log_time',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间'),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='path',
            field=models.TextField(help_text='请求路径', verbose_name='path'),
        ),
    ]
