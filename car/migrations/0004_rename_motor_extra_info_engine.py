# Generated by Django 4.2.1 on 2023-05-28 17:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("car", "0003_alter_car_category_extra_info"),
    ]

    operations = [
        migrations.RenameField(
            model_name="extra_info",
            old_name="motor",
            new_name="engine",
        ),
    ]
