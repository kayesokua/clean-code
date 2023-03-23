STATUS = {
    "OPEN": "open",
    "CLOSED": "closed",
    "REJECTED": "rejected",
    "APPROVED": "approved",
    "PENDING": "pending",
}

MESSAGES = {
    "UPVOTE": "upvote",
    "DOWNVOTE": "downvote",
    "CLOSED": "Merge request has been approved and closed",
    "REJECTED": "Merge request has been rejected and closed",
    "PENDING": "Cannot close merge request until it has been approved or rejected",
    "NO_VOTES": "No votes yet",
    "VOTES": "{} upvotes, {} downvotes",
    "VOTES_UP": "{} upvotes",
    "VOTES_DOWN": "{} downvotes",
    "INVALID_VOTE": "not correct type",
    "INVALID_STATUS": "can't vote on a closed merge request",
}

class MergeRequest:
    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}
        self._status = STATUS["OPEN"]

    def status(self):
        if self._status == STATUS["CLOSED"]:
            return self._status
        elif self._context["downvotes"]:
            return STATUS["REJECTED"]
        elif len(self._context["upvotes"]) >= 2:
            return STATUS["APPROVED"]
        else:
            return STATUS["PENDING"]

    def vote(self, by_user, vote_type):
        if self._status == STATUS["CLOSED"]:
            return "can't vote on a closed merge request"
        if vote_type == "downvote":
            self._context["upvotes"].discard(by_user)
            self._context["downvotes"].add(by_user)
        elif vote_type == "upvote":
            self._context["downvotes"].discard(by_user)
            self._context["upvotes"].add(by_user)
        else:
            return MESSAGES["INVALID_VOTE"]

    def close(self):
        if self.status() == STATUS["APPROVED"]:
            self._status = STATUS["CLOSED"]
            return MESSAGES["CLOSED"]
        elif self.status() == STATUS["REJECTED"]:
            self._status = STATUS["CLOSED"]
            return MESSAGES["REJECTED"]
        else:
            return MESSAGES["PENDING"]

    def getvotes(self):
        upvotes = len(self._context["upvotes"])
        downvotes = len(self._context["downvotes"])
        if upvotes == 0 and downvotes == 0:
            return MESSAGES["NO_VOTES"]
        elif upvotes == 0:
            return MESSAGES["VOTES_DOWN"].format(downvotes)
        elif downvotes == 0:
            return MESSAGES["VOTES_UP"].format(upvotes)
        else:
            return MESSAGES["VOTES"].format(upvotes, downvotes)

example = MergeRequest()
print(example.status())
example.vote("user1", "upvote")
example.vote("user2", "upvote")
example.vote("user3", "downvote")
print(example.getvotes())
print(example.status())
print(example.close())