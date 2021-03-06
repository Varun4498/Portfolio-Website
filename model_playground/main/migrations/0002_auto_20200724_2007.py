# Generated by Django 3.0.8 on 2020-07-24 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='emails',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(unique=True),
        ),
    ]
