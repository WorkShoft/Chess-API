# Generated by Django 3.0.7 on 2020-06-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0025_auto_20200618_1319"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="move", options={"ordering": ["created_at"]},
        ),
        migrations.RenameField(
            model_name="move", old_name="timestamp", new_name="created_at",
        ),
    ]
