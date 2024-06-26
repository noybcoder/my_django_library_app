# Generated by Django 4.2.5 on 2024-04-26 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.language'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('r', 'Reserved'), ('m', 'Maintenance'), ('o', 'On loan')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
