# Generated by Django 3.2.5 on 2021-07-27 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake_shop_app', '0006_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]