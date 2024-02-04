# Generated by Django 4.0.3 on 2024-02-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eqrApp', '0004_employee_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='contact',
            new_name='profession',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.AddField(
            model_name='employee',
            name='boma',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='county',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default='2019-04-05'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_issue',
            field=models.DateField(default='2020-04-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_joining_splm',
            field=models.DateField(default='2021-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='expiry_date',
            field=models.DateField(default='2024-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='payam',
            field=models.CharField(default='11', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
