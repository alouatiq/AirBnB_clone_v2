#!/usr/bin/python3
"""
State module for the HBNB project.

Defines the State class and (for FileStorage) a getter for related City objects.
"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """
    State class for the HBNB project.

    When using DBStorage:
      - __tablename__ is 'states'
      - name is a column (string)
      - cities is a relationship with the City class
    When using FileStorage:
      - name is a string attribute
      - cities is a getter that returns all City objects with state_id == self.id
    """
    __tablename__ = "states"

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan"
        )
    else:
        name = ""

        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equal to the current State id.
            This is only used when FileStorage is enabled.
            """
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
