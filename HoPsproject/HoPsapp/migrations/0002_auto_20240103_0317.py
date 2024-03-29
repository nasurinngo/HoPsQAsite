# Generated by Django 3.2 on 2024-01-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HoPsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoPs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('campusLife', '学校生活'), ('class', '授業'), ('part-timeJob', 'アルバイト'), ('club', 'サークル活動'), ('dreamProject', '夢プロジェクト'), ('entranceExamination', '入試'), ('study', '勉強'), ('seminar', 'ゼミ'), ('departmentalSelection', '学科選択'), ('other', 'その他'), ('wanted', '現在回答募集中の質問')], max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='HoPsModel',
        ),
    ]
