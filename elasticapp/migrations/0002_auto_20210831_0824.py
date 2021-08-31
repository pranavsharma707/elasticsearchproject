# Generated by Django 3.2.6 on 2021-08-31 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, max_length=19, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, max_length=19, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='ElasticDemo',
        ),
    ]
