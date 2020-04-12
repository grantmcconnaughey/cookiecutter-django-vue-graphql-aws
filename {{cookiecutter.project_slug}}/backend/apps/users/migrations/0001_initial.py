from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(blank=True, null=True, verbose_name='last login'),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'username',
                    models.CharField(max_length=255, unique=True, verbose_name='Username'),
                ),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                (
                    'full_name',
                    models.CharField(blank=True, max_length=100, verbose_name='Full name'),
                ),
                (
                    'token',
                    models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Token'),
                ),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                (
                    'registered_at',
                    models.DateTimeField(auto_now_add=True, verbose_name='Registered at'),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users',},
        ),
    ]
