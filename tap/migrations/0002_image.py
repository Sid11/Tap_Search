# Generated by Django 2.2.7 on 2019-12-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
