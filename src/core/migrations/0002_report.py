# Generated by Django 2.0.4 on 2018-07-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_file', models.FileField(upload_to='uploads/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
