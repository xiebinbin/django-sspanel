# Generated by Django 2.0 on 2018-04-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssserver', '0005_auto_20180224_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={'ordering': ['-show', 'level'], 'verbose_name_plural': '节点'},
        ),
    ]