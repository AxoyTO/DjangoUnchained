# Generated by Django 4.0.5 on 2022-06-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
