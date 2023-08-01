# Generated by Django 4.2.3 on 2023-07-25 12:47

from django.db import migrations

import openwisp_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("openwisp_radius", "0034_organizationradiussettings_coa_enabled"),
    ]

    operations = [
        migrations.AddField(
            model_name="organizationradiussettings",
            name="sms_cooldown",
            field=openwisp_utils.fields.FallbackPositiveIntegerField(
                blank=True,
                fallback=30,
                help_text=(
                    "Time period a user will have to wait before"
                    " requesting another SMS token (in seconds)."
                ),
                null=True,
                verbose_name="SMS Cooldown",
            ),
        ),
    ]
