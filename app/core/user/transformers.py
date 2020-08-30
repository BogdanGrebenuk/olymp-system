from app.core.user.domain.entity import User


class UserTransformer:

    async def transform(self, user: User):
        return {
            "id": user.id,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "patronymic": user.patronymic,
            "email": user.email,
            "role": user.role
        }
