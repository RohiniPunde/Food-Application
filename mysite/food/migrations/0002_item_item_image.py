# Generated by Django 3.1.1 on 2020-09-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRQmDtrVAUQIveJQt4rDuLsrEsJ3yyBy24LPg&usqp=CAU', max_length=500),
        ),
    ]