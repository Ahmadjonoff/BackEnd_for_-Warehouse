# Generated by Django 4.0.2 on 2022-02-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='qarz',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='brend',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]