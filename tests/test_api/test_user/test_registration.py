import unittest
from dataclasses import dataclass
from unittest.mock import Mock

from aiohttp.test_utils import (
    AioHTTPTestCase,
    unittest_run_loop
)

from app.main import create_app
from app.core.user.commands import CreateUser
from app.core.user.domain.entity import User
from app.db import mappers_container, UserMapper


class AsyncMock(Mock):

    def __call__(self, *args, **kwargs):
        sup = super(AsyncMock, self)

        async def coro():
            return sup.__call__(*args, **kwargs)
        return coro()

    def __await__(self):
        return self().__await__()


@dataclass
class UserData:
    first_name: str
    last_name: str
    patronymic: str
    email: str
    password: str
    role: str


class RegistrationUnitTests(AioHTTPTestCase):

    async def get_application(self):
        return create_app()

    async def setUpAsync(self):
        self.user_data = UserData(
            first_name="kabab",
            last_name="kabab",
            patronymic="kabab",
            email="kabab@test.com",
            password="Test@123",
            role="participant"
        )

    @unittest_run_loop
    async def test_successful_user_creation(self):
        user_mapper: UserMapper = mappers_container.user_mapper()
        # user_mapper.find_one_by = AsyncMock(return_value=None)
        print(user_mapper.find_one_by)

        bus = self.app['bus']
        user = await bus.execute(
            CreateUser(
                email=self.user_data.email,
                password=self.user_data.password,
                last_name=self.user_data.last_name,
                first_name=self.user_data.first_name,
                patronymic=self.user_data.patronymic,
                role=self.user_data.role
            )
        )

        self.assertIsInstance(user, User)

    @unittest_run_loop
    async def test_successful_user_creation_2(self):
        user_mapper: UserMapper = mappers_container.user_mapper()
        print(user_mapper.find_one_by)
        # user_mapper.find_one_by = AsyncMock(return_value=None)

        bus = self.app['bus']
        user = await bus.execute(
            CreateUser(
                email=self.user_data.email,
                password=self.user_data.password,
                last_name=self.user_data.last_name,
                first_name=self.user_data.first_name,
                patronymic=self.user_data.patronymic,
                role=self.user_data.role
            )
        )

        self.assertIsInstance(user, User)


class TestUnitTests(AioHTTPTestCase):

    async def get_application(self):
        return create_app()

    @unittest_run_loop
    async def test_successful_user_creation(self):
        user_mapper: UserMapper = mappers_container.user_mapper()
        # user_mapper.find_one_by = AsyncMock(return_value=None)
        print(user_mapper.find_one_by)
        user = await user_mapper.find_one_by(email='foo')
        print(user)


if __name__ == '__main__':
    unittest.main()
