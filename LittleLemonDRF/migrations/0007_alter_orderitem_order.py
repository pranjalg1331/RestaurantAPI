# Generated by Django 5.0.1 on 2024-01-06 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0006_remove_cartitem_menuitem_alter_cartitem_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonDRF.order'),
        ),
    ]