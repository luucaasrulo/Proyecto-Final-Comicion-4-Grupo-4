# Generated by Django 4.2.7 on 2023-12-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_resumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
