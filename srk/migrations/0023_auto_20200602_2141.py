# Generated by Django 3.0 on 2020-06-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srk', '0022_employee_kvartira'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dom',
            field=models.IntegerField(max_length=100),
        ),
    ]