from django.db import migrations


def addDefault(apps, schema_editor):
    License = apps.get_model('license', 'License')
    license1 = License(
        id=1,
        title="Trial",
        price=0,
        description="Trial",
        duration=1,
        unlimited=False,
        is_private=True
    )
    license1.save()
    license2 = License(
        id=2,
        title="Forever",
        price=0,
        description="Forever",
        duration=0,
        unlimited=True,
        is_private=True
    )
    license2.save()


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addDefault),
    ]
