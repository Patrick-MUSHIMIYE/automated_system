# Generated by Django 4.2.5 on 2023-10-11 18:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_inquiries', '0005_alter_post_message'),
        ('facilitators', '0002_remove_get_message_reply_alter_get_message_message_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FacPost',
            new_name='FacilitatorReply',
        ),
    ]
