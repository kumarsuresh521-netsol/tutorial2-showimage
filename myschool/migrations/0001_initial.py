# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_rollno', models.IntegerField()),
                ('student_name', models.CharField(max_length=255)),
                ('student_last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=255)),
                ('book_description', models.CharField(max_length=255)),
                ('book_author', models.CharField(max_length=255)),
                ('student', models.ForeignKey(related_name='subjects_students', to='myschool.Students')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='subjects',
            name='teacher',
            field=models.ForeignKey(related_name='subjects_teachers', to='myschool.Teachers'),
        ),
        migrations.AddField(
            model_name='students',
            name='teacher',
            field=models.ForeignKey(related_name='students_teachers', to='myschool.Teachers'),
        ),
    ]
