# Generated by Django 3.2.9 on 2021-11-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='postid',
            field=models.IntegerField(null=True),
        ),
    ]
