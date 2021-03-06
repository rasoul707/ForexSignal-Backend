# Generated by Django 4.0.5 on 2022-07-13 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('license', '0002_auto_20220704_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active_trial', models.BooleanField(
                    default=True, verbose_name='active trial')),
                ('pay_description', models.TextField(default='توضیحات پرداخت')),
                ('terms', models.TextField(default='قوانین')),
                ('trial_license', models.ForeignKey(default=1, null=True,
                 on_delete=django.db.models.deletion.SET_NULL, to='license.license')),
            ],
        ),
    ]
