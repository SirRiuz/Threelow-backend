# Generated by Django 3.2.3 on 2021-08-08 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0005_alter_thread_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='nativeLenguaje',
            field=models.CharField(default='es', max_length=20),
        ),
    ]