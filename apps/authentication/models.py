from django.conf import settings
from django.contrib.auth.models import (
    PermissionsMixin, AbstractUser
)
from datetime import datetime, timedelta
import jwt


class User(AbstractUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)
        token = jwt.encode(payload={
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        },
            key=settings.SECRET_KEY,
            algorithm='HS256'
        )

        # return jwt.decode(
        #     jwt=token,
        #     key=settings.SECRET_KEY,
        #     algorithms='HS256',
        # )
        return token.decode('utf-8')



