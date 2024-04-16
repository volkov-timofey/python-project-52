# Generated by Django 5.0.2 on 2024-04-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('describe', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]