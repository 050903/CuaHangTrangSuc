# Generated by Django 5.1.5 on 2025-01-30 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UuDaiKhachHang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ma_khach_hang', models.CharField(max_length=20)),
                ('phan_tram_chiet_khau', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duoc_duyet', models.BooleanField(default=False)),
            ],
        ),
    ]
