# Generated by Django 4.0.5 on 2022-06-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('github_Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(default=None, upload_to='images/languages/')),
                ('version', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('technologies_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Project.technologies')),
            ],
            bases=('Project.technologies',),
        ),
        migrations.CreateModel(
            name='Operating_System',
            fields=[
                ('technologies_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Project.technologies')),
            ],
            bases=('Project.technologies',),
        ),
        migrations.CreateModel(
            name='Programming_Language',
            fields=[
                ('technologies_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Project.technologies')),
            ],
            bases=('Project.technologies',),
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('technologies_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Project.technologies')),
            ],
            bases=('Project.technologies',),
        ),
        migrations.CreateModel(
            name='Project_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgCode', models.CharField(max_length=12, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default=None, upload_to='images/projects')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='frameworks',
            field=models.ManyToManyField(blank=True, to='Project.framework'),
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(to='Project.programming_language'),
        ),
        migrations.AddField(
            model_name='project',
            name='o_Systems',
            field=models.ManyToManyField(to='Project.operating_system'),
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(blank=True, to='Project.tool'),
        ),
    ]