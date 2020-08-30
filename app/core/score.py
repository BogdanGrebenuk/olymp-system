from collections import defaultdict

from typing import List

from app.db.entities import Solution, Contest


# todo: refactor..
def get_total_score(contest: Contest, solutions: List[Solution]):
    solutions_by_tasks = defaultdict(list)
    for solution in solutions:
        solutions_by_tasks[solution.task_id].append(solution)

    acc = 0
    end_at = contest.end_date.timestamp()
    for task_id in solutions_by_tasks:
        sorted_solutions = sorted(
            solutions_by_tasks[task_id],
            key=lambda s: (s.is_passed, s.created_at)
        )
        for solution in sorted_solutions:
            if not solution.is_passed:
                acc -= 1200  # penalty is 20 minutes
            else:
                acc += int(end_at - solution.created_at.timestamp())
                break
    return acc
