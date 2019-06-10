# Generated by Django 2.2.1 on 2019-06-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogmahdi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]