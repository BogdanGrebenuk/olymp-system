# import importlib
# from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
#
# import app.main as main
# # from app.main import create_app
# from app.db import mappers_container, UserMapper
#
#
# class MockTests(AioHTTPTestCase):
#
#     async def get_application(self):
#         # importlib.reload(main)
#         return main.create_app()
#
#     @unittest_run_loop
#     async def test_mock(self):
#         print('mock')
#         user_mapper = mappers_container.user_mapper()
#         print(await user_mapper.find_one_by(email="kabab@test.com"))
