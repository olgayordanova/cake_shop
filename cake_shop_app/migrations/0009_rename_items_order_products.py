# Generated by Django 3.2.5 on 2021-07-27 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake_shop_app', '0008_auto_20210727_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='products',
        ),
    ]
