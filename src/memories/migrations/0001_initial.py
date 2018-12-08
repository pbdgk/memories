# Generated by Django 2.1.4 on 2018-12-08 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import memories.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('media', models.FileField(blank=True, null=True, upload_to=memories.models.user_directory_path)),
                ('embed_id', models.CharField(blank=True, default='', max_length=50)),
                ('created', models.DateTimeField()),
                ('mime_type', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
