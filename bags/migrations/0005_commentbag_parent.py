# Generated by Django 3.0.7 on 2020-11-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0004_auto_20201130_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentbag',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='bags.CommentBag'),
        ),
    ]