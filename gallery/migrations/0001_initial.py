# Generated by Django 4.0.3 on 2022-04-13 14:20

from django.db import migrations, models
import gallery.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='bb26a162fc1d4f319604bfd35994e088', max_length=64)),
                ('slug', models.SlugField(default='<django.db.models.fields.CharField>', max_length=64)),
                ('photo', models.ImageField(upload_to=gallery.utils.path_rename)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('photo', models.ManyToManyField(to='gallery.photo')),
            ],
        ),
    ]
