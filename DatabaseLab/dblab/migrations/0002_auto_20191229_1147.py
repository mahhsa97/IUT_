# Generated by Django 2.1.15 on 2019-12-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dblab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('ID1', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('ID1', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('ID1', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID1', models.CharField(max_length=5, unique=True)),
                ('Description', models.CharField(max_length=100)),
                ('PostDate', models.DateTimeField(auto_now_add=True)),
                ('ExpirationDate', models.DateTimeField()),
                ('isExpired', models.BooleanField()),
                ('Price', models.IntegerField()),
                ('forBorrow', models.BooleanField()),
                ('CityID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.City')),
                ('CountryID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Country')),
            ],
        ),
        migrations.CreateModel(
            name='ProvideService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID1', models.CharField(max_length=5, unique=True)),
                ('Description', models.CharField(max_length=100)),
                ('PostDate', models.DateTimeField(auto_now_add=True)),
                ('ExpirationDate', models.DateTimeField()),
                ('isExpired', models.BooleanField()),
                ('Price', models.IntegerField()),
                ('CategoryID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Categories')),
                ('CityID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.City')),
                ('CountryID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Country')),
            ],
        ),
        migrations.CreateModel(
            name='RequestProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID1', models.CharField(max_length=5, unique=True)),
                ('Description', models.CharField(max_length=100)),
                ('PostDate', models.DateTimeField(auto_now_add=True)),
                ('ExpirationDate', models.DateTimeField()),
                ('isExpired', models.BooleanField()),
                ('Price', models.IntegerField()),
                ('CityID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.City')),
                ('CountryID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Country')),
            ],
        ),
        migrations.CreateModel(
            name='RequestService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID1', models.CharField(max_length=5, unique=True)),
                ('Description', models.CharField(max_length=100)),
                ('PostDate', models.DateTimeField(auto_now_add=True)),
                ('ExpirationDate', models.DateTimeField()),
                ('isExpired', models.BooleanField()),
                ('Price', models.IntegerField()),
                ('CategoryID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Categories')),
                ('CityID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.City')),
                ('CountryID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=20)),
                ('UserName', models.CharField(max_length=5, unique=True)),
                ('Description', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=20)),
                ('CityID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.City')),
                ('CountryID', models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Country')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='requestservice',
            name='UserName',
            field=models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Users'),
        ),
        migrations.AddField(
            model_name='requestproduct',
            name='UserName',
            field=models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Users'),
        ),
        migrations.AddField(
            model_name='provideservice',
            name='UserName',
            field=models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Users'),
        ),
        migrations.AddField(
            model_name='productsale',
            name='UserName',
            field=models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Users'),
        ),
        migrations.AddField(
            model_name='city',
            name='CountryID',
            field=models.ForeignKey(on_delete='cascade', related_name='+', to='dblab.Country'),
        ),
    ]
