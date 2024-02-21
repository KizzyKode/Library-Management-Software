

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0015_student_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Registereduser',
        ),
        migrations.RenameField(
            model_name='issuedbook',
            old_name='student_id',
            new_name='registereduser_id',
        ),
    ]
