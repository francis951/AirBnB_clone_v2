#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """instance initialization"""
        super().__init__(*args, **kwargs)
