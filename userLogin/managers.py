from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, uid, password, **extra_fields):
        """
        Creates and saves a User with the given uid, email and password.
        """
        if not uid:
            raise ValueError('The given userid must be set')
        uid = self.normalize_email(uid)
        user = self.model(uid=uid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, uid, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(uid, password, **extra_fields)

    def create_superuser(self, uid, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(uid, password, **extra_fields)