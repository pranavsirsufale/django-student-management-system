# Generated by Django 4.2.3 on 2023-08-21 10:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0010_staff_feeback"),
    ]

    operations = [
        migrations.RenameField(
            model_name="staff_feeback",
            old_name="reedback",
            new_name="feedback",
        ),
    ]
