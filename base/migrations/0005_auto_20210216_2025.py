# Generated by Django 3.1.6 on 2021-02-16 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210216_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingadress',
            old_name='postCode',
            new_name='postalCode',
        ),
    ]