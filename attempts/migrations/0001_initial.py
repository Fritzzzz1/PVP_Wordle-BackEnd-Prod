# Generated by Django 4.0.4 on 2022-05-07 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=6)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempt', to='boards.board')),
            ],
        ),
    ]