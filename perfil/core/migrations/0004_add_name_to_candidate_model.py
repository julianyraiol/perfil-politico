# Generated by Django 2.1.1 on 2018-09-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0003_create_index_for_related_models")]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="name",
            field=models.CharField(blank=True, default="", max_length=128),
        )
    ]