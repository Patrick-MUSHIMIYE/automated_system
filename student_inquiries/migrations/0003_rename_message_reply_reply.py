# Generated by Django 4.2.5 on 2023-10-10 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_inquiries', '0002_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='message',
            new_name='reply',
        ),
    ]