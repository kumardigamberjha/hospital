# Generated by Django 4.0.1 on 2022-04-04 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check_In_Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chkin', models.BooleanField()),
                ('chkin_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('phn', models.IntegerField()),
                ('disease', models.CharField(max_length=50)),
            ],
        ),
            migrations.AddField(
                model_name='check_in_model',
                name='user',
                field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.user_data'),
            ),
        
        migrations.CreateModel(
            name='Check_Out_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chkout', models.BooleanField()),
                ('chkout_date', models.DateTimeField(auto_now=True)),
                ('chkedin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.check_in_model')),
            ],
        ),
    ]