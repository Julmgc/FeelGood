# Generated by Django 4.0.3 on 2022-03-24 23:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=9)),
                ('house_number', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
