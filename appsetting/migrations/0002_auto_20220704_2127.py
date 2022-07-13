from django.db import migrations


def addDefault(apps, schema_editor):
    AppSetting = apps.get_model('appsetting', 'AppSetting')
    setting = AppSetting()
    setting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('appsetting', '0001_initial')
    ]

    operations = [
        migrations.RunPython(addDefault)
    ]
