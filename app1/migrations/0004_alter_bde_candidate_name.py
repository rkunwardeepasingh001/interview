# Generated by Django 4.2.7 on 2023-12-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_rename_name_bde_candidate_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bde",
            name="candidate_name",
            field=models.CharField(max_length=50),
        ),
    ]
