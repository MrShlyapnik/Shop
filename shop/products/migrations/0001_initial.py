# Generated by Django 2.2.4 on 2019-08-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('supplier', models.CharField(max_length=64)),
                ('buy_count', models.IntegerField()),
            ],
        ),
    ]
