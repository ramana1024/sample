# Generated by Django 3.0.3 on 2020-02-10 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryformapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquirydata',
            old_name='location',
            new_name='locations',
        ),
    ]