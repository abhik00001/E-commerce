# Generated by Django 5.0.3 on 2024-03-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field=360, null=True, upload_to='product_images', width_field=640),
        ),
    ]