import uuid
from functools import partial

from aiopg.sa import Engine
from concurrent.futures import ThreadPoolExecutor

from app.utils.executor import Executor

from app.commandbus.command_handlers.base_command_handler import CommandHandler
from app.commandbus.bus import Bus
from app.core.contest.commands.create_contest import CreateContest
from app.core.contest.services import ImagePathGenerator
from app.core.contest.domain.entity import Contest
from app.db.mappers.contest import ContestMapper
from app.common import ROOT_DIR
from app.utils.filesystem import save_file_field_image


class CreateContestHandler(CommandHandler):
    def __init__(
            self,
            engine: Engine,
            executor: Executor,
            thread_pool: ThreadPoolExecutor,
            bus: Bus,
            contest_mapper: ContestMapper,
            image_path_generator: ImagePathGenerator
    ):
        self.engine = engine
        self.executor = executor
        self.thread_pool = thread_pool
        self.bus = bus
        self.contest_mapper = contest_mapper
        self.image_path_generator = image_path_generator

    async def handle(self, command: CreateContest):
        image = command.image

        image_path = None
        if image is not None:
            image_path = self.image_path_generator.generate(image)
            task = partial(save_file_field_image, image.file, image_path)
            await self.executor.run(task, self.thread_pool)
            image_path = str(image_path.relative_to(ROOT_DIR))

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
        await self.contest_mapper.create(contest)
        return contest
