# Generated by Django 4.0.5 on 2022-07-27 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_num', models.IntegerField(primary_key=True, serialize=False)),
                ('post_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_num', models.IntegerField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.post')),
            ],
        ),
    ]
