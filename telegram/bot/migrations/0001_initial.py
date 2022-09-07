# Generated by Django 4.1 on 2022-08-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatbotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(verbose_name='Chat ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='Full name')),
                ('username', models.CharField(max_length=500, verbose_name='Username')),
                ('language_code', models.CharField(max_length=500, verbose_name='Language')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='MessageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField(verbose_name='Message ID')),
                ('chat_id', models.IntegerField(verbose_name='Chat ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='Full name')),
                ('username', models.CharField(max_length=500, verbose_name='Username')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('text', models.CharField(max_length=1500, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
    ]
