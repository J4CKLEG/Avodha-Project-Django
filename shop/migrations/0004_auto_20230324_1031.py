# Generated by Django 2.2 on 2023-03-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20230321_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categ',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
