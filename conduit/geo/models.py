from decimal import Decimal
import datetime as dt
from flask_jwt_extended.jwt_manager import JWTManager
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy

from conduit.database import (Model, SurrogatePK, db, Column,
                              reference_col, relationship)
from conduit.profile.models import UserProfile


class Geolocation(Model, SurrogatePK):
    __tablename__ = 'geo_locations'

    id = Column(db.Integer, primary_key=True)
    eid = Column(db.VARCHAR, nullable=False)
    entity = Column(db.Text)
    lat = Column(db.DECIMAL, nullable=False)
    lon = Column(db.DECIMAL, nullable=False)

    def __init__(self, eid: int, lat: Decimal, lon: Decimal, **kwargs):
        db.Model.__init__(self, eid=eid, lat=lat, lon=lon, **kwargs)

