# Generated by Django 3.1 on 2020-09-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desciption',
            field=models.TextField(default=1, max_length=1028),
            preserve_default=False,
        ),
    ]