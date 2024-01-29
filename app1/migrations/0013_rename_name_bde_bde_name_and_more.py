# Generated by Django 4.2.7 on 2023-12-14 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0012_alter_questions_company_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bde",
            old_name="name",
            new_name="bde_name",
        ),
        migrations.AlterField(
            model_name="interview",
            name="scheduled_by",
            field=models.ForeignKey(
                max_length=20,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app1.bde",
            ),
        ),
    ]
