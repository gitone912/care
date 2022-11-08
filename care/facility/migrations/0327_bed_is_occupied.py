# Generated by Django 2.2.11 on 2022-11-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0326_auto_20221018_1526'),
    ]
    
    def update_previous_beds(apps, schema_editor):
        Bed = apps.get_model('facility', 'Bed')
        ConsultationBed = apps.get_model('facility', 'ConsultationBed')
        for bed in Bed.objects.all():
            bed.is_occupied = ConsultationBed.objects.filter(bed=bed, end_date__isnull=True).exists()
            bed.save()

    operations = [
        migrations.AddField(
            model_name='bed',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(update_previous_beds)
    ]

