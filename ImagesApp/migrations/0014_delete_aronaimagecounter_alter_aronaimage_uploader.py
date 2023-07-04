# Generated by Django 4.1 on 2023-04-18 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0004_followrelation_remove_user_followers'),
        ('ImagesApp', '0013_aronaimage_comments_aronaimage_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AronaImageCounter',
        ),
        migrations.AlterField(
            model_name='aronaimage',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.user'),
        ),
    ]