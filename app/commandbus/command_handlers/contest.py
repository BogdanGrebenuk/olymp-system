import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.contest import CreateContest, SaveContestImage
from common import ROOT_DIR
from db.entities.contest import Contest
from db.procedures.contest import create_contest


class CreateContestHandler(CommandHandler):

    async def handle(self, command: CreateContest):
        engine = command.engine
        image_path = str(uuid.uuid4())
        await self.bus.execute(SaveContestImage(command.image, image_path))

        contest_id = str(uuid.uuid4())
        contest = Contest(contest_id, command.name, command.description, image_path)
        await create_contest(engine, contest)
        return contest


class SaveContestImageHandler(CommandHandler):

    async def handle(self, command: SaveContestImage):
        image_path = ROOT_DIR / f"public/{command.img_path}"

        with open(image_path, "wb") as file:
            file.write(command.img)

        return image_path

