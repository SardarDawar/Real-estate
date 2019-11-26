# Generated by Django 2.2.6 on 2019-11-22 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactNumber', models.IntegerField(blank=True, null=True)),
                ('approve', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Teacher_or_Parent', models.CharField(blank=True, choices=[('Buyer', 'Buyer'), ('Agent', 'Agent')], default='Buyer', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]