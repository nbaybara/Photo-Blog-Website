# Generated by Django 3.1.dev20200327073858 on 2020-05-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200510_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]
