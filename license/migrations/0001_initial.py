# Generated by Django 4.0.5 on 2022-07-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('is_private', models.BooleanField(default=False, verbose_name='private')),
                ('unlimited', models.BooleanField(default=False, verbose_name='unlimited')),
                ('duration', models.DurationField()),
            ],
        ),
    ]
