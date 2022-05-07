# Generated by Django 4.0.2 on 2022-02-09 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0003_remove_client_ism'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('umumiy', models.PositiveSmallIntegerField()),
                ('tolandi', models.PositiveSmallIntegerField()),
                ('nasiya', models.PositiveSmallIntegerField()),
                ('sana', models.DateTimeField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.client')),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.mahsulot')),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.ombor')),
            ],
        ),
    ]
