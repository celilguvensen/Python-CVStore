# Generated by Django 4.1 on 2022-12-07 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_profile_address"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile", options={"ordering": ["-created_date"]},
        ),
    ]
