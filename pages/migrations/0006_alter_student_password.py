# Generated by Django 4.1.7 on 2023-06-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_onlinetest_onlinereklama_alter_blogtable_blogtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
