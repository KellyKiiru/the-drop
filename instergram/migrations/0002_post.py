# Generated by Django 4.0.4 on 2022-06-08 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instergram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='static/', verbose_name='Picture')),
                ('caption', models.CharField(max_length=500, verbose_name='Caption')),
                ('posted', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instergram.profile')),
            ],
        ),
    ]
