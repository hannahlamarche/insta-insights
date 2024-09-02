from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime
from .Account import Account
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class Report(BaseModel):
    username: str
    date: datetime
    followers: List[Account]
    following: List[Account]
    dont_follow_me_back: List[Account]
    i_dont_follow_back: List[Account]
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "username": "user.name",
                "date": "2024-09-01T00:00:00Z",
                "followers": [
                    {
                        "username": "follower1",
                        "full_name": "Follower One"
                    }
                ],
                "following": [
                    {
                        "username": "following1",
                        "full_name": "Following One"
                    }
                ],
                "dont_follow_me_back": [
                    {
                        "username": "dont_follow_me_back1",
                        "full_name": "Not Following Back One"
                    }
                ],
                "i_dont_follow_back": [
                    {
                        "username": "i_dont_follow_back1",
                        "full_name": "I Don't Follow Back One"
                    }
                ]
            }
        },
    )
