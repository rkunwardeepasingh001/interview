# Generated by Django 4.2.7 on 2023-12-14 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0011_alter_interview_company_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="company_name",
            field=models.ForeignKey(
                max_length=20,
                on_delete=django.db.models.deletion.CASCADE,
                to="app1.company",
            ),
        ),
    ]
