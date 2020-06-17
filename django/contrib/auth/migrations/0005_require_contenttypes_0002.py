# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0004_alter_user_username_opts'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        # Ensure the contenttypes migration is applied before sending
        # post_migrate signals (which create ContentTypes).
    ]
