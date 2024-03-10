#!/usr/bin/python3


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def save(self):
        """"""
        """"""
        self.update_at = datetime.now()

    def to_dict(self):
        """"""
        """"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["crated_at"] = self.created_at.isoformat()
        inst_dict["update_at"] = self.update_at.isoformat()
        return inst_dict

    def __str__(self):
        """"""
        """"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
