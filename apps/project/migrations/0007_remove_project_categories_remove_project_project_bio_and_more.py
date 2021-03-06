# Generated by Django 4.0.5 on 2022-07-09 17:46

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_database_library_other_projecttype_and_more'),
        ('project', '0006_remove_project_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_bio',
        ),
        migrations.AddField(
            model_name='project',
            name='databases',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='category.database'),
        ),
        migrations.AddField(
            model_name='project',
            name='demo_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='frameworks',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='category.framework'),
        ),
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='category.language'),
        ),
        migrations.AddField(
            model_name='project',
            name='libraries',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='category.library'),
        ),
        migrations.AddField(
            model_name='project',
            name='others',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='category.other'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='category.projecttype'),
        ),
    ]
