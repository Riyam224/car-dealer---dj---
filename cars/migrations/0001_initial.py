# Generated by Django 3.1.5 on 2021-01-14 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=100)),
                ('image_main', models.ImageField(upload_to='images')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images')),
                ('miles', models.IntegerField(blank=True, null=True)),
                ('transission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=100)),
                ('year', models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021, verbose_name='year')),
                ('power', models.IntegerField()),
                ('fuel', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dealers.dealer', verbose_name='dealer')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
