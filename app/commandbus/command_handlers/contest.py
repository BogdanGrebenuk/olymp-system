import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.contest import CreateContest, SaveContestImage
from common import ROOT_DIR, PUBLIC_DIR
from db.entities.contest import Contest
from db.procedures.contest import create_contest


class CreateContestHandler(CommandHandler):

    async def handle(self, command: CreateContest):
        engine = command.engine
        image = command.image

        if image is None:  # TODO: remove it to another handler/function
            image_path = None
        else:
            path = PUBLIC_DIR / f"{uuid.uuid4()}{image.filename}"
            await self.bus.execute(
                SaveContestImage(image.file.read(), path)
            )
            image_path = str(path.relative_to(ROOT_DIR))

        contest_id = str(uuid.uuid4())
        contest = Contest(
            contest_id,
            command.name,
            command.description,
            image_path
        )
        await create_contest(engine, contest)
        return contest


class SaveContestImageHandler(CommandHandler):

    async def handle(self, command: SaveContestImage):
        image_path = command.image_path
        image_bytes = command.image_bytes
        with open(image_path, "wb") as file:  # TODO: execute it in pool
            file.write(image_bytes)
