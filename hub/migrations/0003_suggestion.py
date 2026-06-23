from django.db import migrations, models


def seed_suggestions(apps, schema_editor):
    Suggestion = apps.get_model('hub', 'Suggestion')
    Suggestion.objects.bulk_create([
        Suggestion(
            title='Morning Meditation',
            description='Start your day with mindfulness.',
            icon='🌅',
            order=1,
        ),
        Suggestion(
            title='Read: "Atomic Habits"',
            description='by James Clear.',
            icon='📖',
            order=2,
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_todoitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('icon', models.CharField(default='💡', max_length=10)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order', 'title'],
            },
        ),
        migrations.RunPython(seed_suggestions, migrations.RunPython.noop),
    ]
