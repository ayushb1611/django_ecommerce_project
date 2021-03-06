# Generated by Django 4.0.4 on 2022-06-16 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_specifications', models.TextField()),
                ('product_stock', models.IntegerField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='filepath')),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
