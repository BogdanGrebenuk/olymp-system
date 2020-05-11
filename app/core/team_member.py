from enum import Enum


class MemberStatus(Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    DECLINED = 'declined'


class MemberStatusAction(Enum):
    ACCEPT = 'accept'
    DECLINE = 'decline'


def get_member_status_actions():
    return [i.value for i in MemberStatusAction]


def get_status_by_action(action: str) -> MemberStatus:
    if action == MemberStatusAction.ACCEPT.value:
        return MemberStatus.ACCEPTED
    elif action == MemberStatusAction.DECLINE.value:
        return MemberStatus.DECLINED
    raise ValueError(f'unknown action {action}!')
