# Generated by Django 5.1.3 on 2024-11-24 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lf', models.CharField(max_length=32)),
                ('si', models.CharField(max_length=32)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('relative', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True)),
                ('village', models.CharField(blank=True, max_length=255, null=True)),
                ('panchayat', models.CharField(blank=True, max_length=255, null=True)),
                ('block', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('aadhar', models.CharField(blank=True, max_length=12, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('site', models.CharField(blank=True, max_length=255, null=True)),
                ('thana', models.CharField(blank=True, max_length=255, null=True)),
                ('khata', models.CharField(blank=True, max_length=255, null=True)),
                ('khesra', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.FloatField(default=0)),
                ('farmer_type', models.CharField(choices=[('LL', 'Landless Farmer'), ('MF', 'Marginal Farmer'), ('SF', 'Small Farmer'), ('BF', 'Big Farmer')], max_length=2)),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='certificates/')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='signatures/')),
                ('lno', models.CharField(blank=True, max_length=32, null=True)),
                ('grno', models.CharField(blank=True, max_length=32, null=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
