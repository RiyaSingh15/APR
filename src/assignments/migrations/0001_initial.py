# Generated by Django 3.0.3 on 2020-07-04 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_video_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Instructions', models.CharField(default=None, max_length=1000, null=True)),
                ('Deadline', models.DateTimeField(default=None, null=True)),
                ('Posted', models.DateTimeField(auto_now_add=True)),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='lessons.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdf', to='assignments.assignment')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_pdfs', to='lessons.Lesson')),
                ('pdf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_pdfs', to='accounts.pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Duration', models.CharField(max_length=10)),
                ('final', models.BooleanField(default=False)),
                ('Assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test', to='assignments.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='assignments.assignment')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_videos', to='lessons.Lesson')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_videos', to='accounts.video')),
            ],
        ),
        migrations.CreateModel(
            name='user_progress_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watched_assignment_video', to=settings.AUTH_USER_MODEL)),
                ('Video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_video', to='assignments.Video')),
            ],
        ),
        migrations.CreateModel(
            name='user_progress_pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Pdf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pdf', to='assignments.Pdf')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='read_assignment_pdf', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_test_questions', to='lessons.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='assignments.Test')),
            ],
        ),
        migrations.CreateModel(
            name='assignment_video_likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('AComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.AComment')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_video_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='acomment',
            name='Video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='assignments.Video'),
        ),
        migrations.AddField(
            model_name='acomment',
            name='likes',
            field=models.ManyToManyField(through='assignments.assignment_video_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='acomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='assignments.AComment'),
        ),
    ]
