# Generated by Django 4.1 on 2022-12-22 13:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resumes", "0004_alter_resume_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="content",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Ön Yazı"
            ),
        ),
    ]
