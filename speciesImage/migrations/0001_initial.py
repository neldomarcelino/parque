# Generated by Django 2.2.7 on 2021-05-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecieImage',
            fields=[
                ('id_image', models.AutoField(db_column='idImage', primary_key=True, serialize=False)),
                ('description', models.TextField(db_column='descricao', null=True)),
                ('image', models.FileField(upload_to='image')),
            ],
            options={
                'db_table': 'especieimage',
                'managed': False,
            },
        ),
    ]
