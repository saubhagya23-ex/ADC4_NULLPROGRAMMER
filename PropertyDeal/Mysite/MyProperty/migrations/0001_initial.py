# Generated by Django 2.2.7 on 2020-01-10 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=50)),
                ('registry_no', models.CharField(max_length=100)),
                ('property_pic', models.ImageField(upload_to='media/')),
                ('property_type', models.CharField(max_length=50)),
                ('property_style', models.CharField(max_length=50)),
                ('property_region', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=5)),
                ('no_of_kitchen', models.CharField(max_length=5)),
                ('no_of_bedroom', models.CharField(max_length=5)),
                ('no_of_bathroom', models.CharField(max_length=5)),
                ('year_built', models.CharField(max_length=5)),
                ('price', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_no', models.CharField(max_length=50)),
                ('registry_no', models.CharField(max_length=100)),
                ('property_pic', models.ImageField(upload_to='media/')),
                ('property_type', models.CharField(max_length=50)),
                ('property_style', models.CharField(max_length=50)),
                ('property_region', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=5)),
                ('no_of_kitchen', models.CharField(max_length=5)),
                ('no_of_bedroom', models.CharField(max_length=5)),
                ('no_of_bathroom', models.CharField(max_length=5)),
                ('year_built', models.CharField(max_length=5)),
                ('price', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='landOwnerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('contact_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=2000)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('pin', models.IntegerField(verbose_name=6)),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyProperty.land')),
            ],
        ),
        migrations.CreateModel(
            name='landAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=50)),
                ('sec', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pin', models.IntegerField(verbose_name=6)),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyProperty.land')),
            ],
        ),
        migrations.CreateModel(
            name='HouseOwnerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('contact_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=2000)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('pin', models.IntegerField(verbose_name=6)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyProperty.House')),
            ],
        ),
        migrations.CreateModel(
            name='HouseAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=50)),
                ('sec', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pin', models.IntegerField(verbose_name=6)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyProperty.House')),
            ],
        ),
    ]