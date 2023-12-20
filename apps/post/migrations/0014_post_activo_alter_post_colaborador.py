# Generated by Django 4.2.7 on 2023-12-13 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0013_alter_post_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='colaborador',
            field=models.ForeignKey(default='desconocido', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]