# Generated by Django 4.2 on 2023-04-08 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatTranslation', '0004_alter_user_img_alter_user_unique_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incoming_msg_id', models.IntegerField()),
                ('outgoing_msg_id', models.IntegerField()),
                ('msg', models.CharField(max_length=1000)),
                ('translated_msg', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'message',
                'db_table_comment': 'Chat and Translated Message',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.IntegerField(default=1613560319),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]