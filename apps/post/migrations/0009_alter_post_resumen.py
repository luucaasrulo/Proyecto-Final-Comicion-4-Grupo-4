# Generated by Django 4.2.7 on 2023-12-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_resumen_alter_post_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resumen',
            field=models.CharField(max_length=100),
        ),
    ]
