# Generated by Django 2.2 on 2020-09-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wordlist4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'wordlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wordlist6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'wordlist6',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RankScoreList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
