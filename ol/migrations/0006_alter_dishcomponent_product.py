# Generated by Django 4.0.1 on 2022-01-11 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ol', '0005_alter_dishcomponent_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishcomponent',
            name='product',
            field=models.ForeignKey(default='отсутствует', on_delete=django.db.models.deletion.CASCADE, to='ol.product', to_field='name'),
        ),
    ]