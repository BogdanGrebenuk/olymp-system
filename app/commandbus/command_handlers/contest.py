import uuid
from functools import partial

import utils.executor as executor
from db import contest_mapper
from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.contest import CreateContest, GenerateContestImagePath
from common import ROOT_DIR, PUBLIC_DIR
from db.entities.contest import Contest
from utils.filesystem import save_file_field_image


class CreateContestHandler(CommandHandler):

    async def handle(self, command: CreateContest):
        engine = command.engine
        image = command.image
        thread_pool = command.pool

        image_path = None
        if image is not None:
            image_path = await self.bus.execute(GenerateContestImagePath(image))
            task = partial(save_file_field_image, image.file, image_path)
            await executor.run(task, thread_pool)

        contest_id = str(uuid.uuid4())
        contest = Contest(
            id=contest_id,
            name=command.name,
            description=command.description,
            max_teams=command.max_teams,
            max_participants_in_team=command.max_participants_in_team,
            image_path=image_path,
            start_date=command.start_date,
            end_date=command.end_date,
            creator_id=command.creator_id
        )
        await contest_mapper.create(engine, contest)
        return contest


class GenerateContestImagePathHandler(CommandHandler):

    async def handle(self, command: GenerateContestImagePath):
        image = command.image
        image_path = PUBLIC_DIR / f"{uuid.uuid4()}{image.filename}"
        return str(image_path.relative_to(ROOT_DIR))
