# Generated by Django 3.1.7 on 2021-07-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('task', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('deadline', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
    ]
