# Generated by Django 4.1 on 2022-12-22 08:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resumes", "0002_alter_resume_content_alter_resume_position_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="content",
            field=ckeditor.fields.RichTextField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="Ön Yazı (Max 500 karakter Giriniz)",
            ),
        ),
    ]
