# Generated by Django 3.0.2 on 2020-02-01 17:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment',
                 models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='concierge.Apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='KeyTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_out_date', models.DateTimeField(null=True)),
                ('key_in_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('key_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='concierge.Key')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='concierge.Person')),
            ],
        ),
    ]
