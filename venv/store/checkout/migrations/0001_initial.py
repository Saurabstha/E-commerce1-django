# Generated by Django 2.2.7 on 2019-12-10 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('first_address', models.CharField(max_length=30)),
                ('second_address', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('sub_total', models.FloatField(default=0)),
                ('shipping', models.FloatField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('order_total', models.FloatField(default=0)),
                ('products', models.ManyToManyField(to='cart.Cart')),
            ],
        ),
    ]
