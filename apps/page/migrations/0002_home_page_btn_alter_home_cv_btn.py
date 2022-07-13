# Generated by Django 4.0.5 on 2022-07-10 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtaildocs', '0012_uploadeddocument'),
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='page_btn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='home',
            name='cv_btn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]
