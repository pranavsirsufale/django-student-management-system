# Generated by Django 4.2.3 on 2023-08-21 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_staff_notification_statuss"),
    ]

    operations = [
        migrations.CreateModel(
            name="Staff_leave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.CharField(max_length=100)),
                ("message", models.TextField()),
                ("statuss", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.staff"
                    ),
                ),
            ],
        ),
    ]