# Generated by Django 4.1.7 on 2023-06-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]