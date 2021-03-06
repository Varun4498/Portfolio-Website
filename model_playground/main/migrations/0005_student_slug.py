# Generated by Django 3.0.8 on 2020-07-24 20:37

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
    ]
