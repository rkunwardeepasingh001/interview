# Generated by Django 4.2.7 on 2023-12-13 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_alter_bde_interview_schedule"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bde",
            old_name="name",
            new_name="candidate_name",
        ),
        migrations.RenameField(
            model_name="bde",
            old_name="interview_schedule",
            new_name="interview_schedule_date",
        ),
    ]
