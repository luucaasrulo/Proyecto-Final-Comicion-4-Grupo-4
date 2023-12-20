# Generated by Django 4.2.7 on 2023-12-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_post_activo_alter_post_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(default='desconocido', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='post/imagen_programacion.jpg', help_text='imagen 16:9 ó 370x140px', null=True, upload_to='post'),
        ),
    ]