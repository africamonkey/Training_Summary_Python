# Generated by Django 2.0.3 on 2018-03-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('num_of_problem', models.IntegerField(choices=[('5 - E', 5), ('6 - F', 6), ('7 - G', 7), ('8 - H', 8), ('9 - I', 9), ('10 - J', 10), ('11 - K', 11), ('12 - L', 12), ('13 - M', 13)], default='5 - E')),
            ],
        ),
    ]
