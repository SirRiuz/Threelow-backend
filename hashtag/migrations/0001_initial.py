# Generated by Django 3.2.3 on 2021-07-11 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('threads', '0005_alter_thread_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(max_length=50)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threads.thread')),
            ],
        ),
    ]
