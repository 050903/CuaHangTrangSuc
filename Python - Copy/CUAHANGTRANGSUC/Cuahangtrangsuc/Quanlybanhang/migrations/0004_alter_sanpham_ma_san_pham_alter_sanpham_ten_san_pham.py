# Generated by Django 5.1.5 on 2025-01-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quanlybanhang', '0003_uudaikhachhang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='ma_san_pham',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sanpham',
            name='ten_san_pham',
            field=models.CharField(max_length=255),
        ),
    ]
