# Generated by Django 4.0.4 on 2022-07-19 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forum_amo", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="duvida",
            name="arquivo",
        ),
        migrations.RemoveField(
            model_name="duvida",
            name="privacidade_autor",
        ),
    ]
