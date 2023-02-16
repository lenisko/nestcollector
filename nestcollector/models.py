"""
Module containing model database definitions.
"""

from sqlalchemy import Column, Float, Index, String, func, text
from sqlalchemy.types import UserDefinedType
from sqlalchemy.dialects.mysql import BIGINT, DECIMAL, LONGTEXT, INTEGER, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Geometry(UserDefinedType):
    """
    Represents a geometry column in the database.
    """

    def get_col_spec(self):
        return 'GEOMETRY'

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ST_AsText(col, type_=self)


class Nest(Base):
    """
    Represents a nest in the database.
    """
    __tablename__ = 'nests'
    __table_args__ = (
        Index('CoordsIndex', 'lat', 'lon'),
    )

    nest_id = Column(BIGINT(20), primary_key=True)
    lat = Column(Float(18, True), nullable=False)
    lon = Column(Float(18, True), nullable=False)
    polygon_type = Column(TINYINT(1), nullable=False)
    polygon_path = Column(LONGTEXT, nullable=False)
    type = Column(TINYINT(1), nullable=False, server_default=text('0'))
    name = Column(String(250))
    spawnpoints = Column(TINYINT(4), server_default=text('0'))
    m2 = Column(DECIMAL(10, 1), server_default=text('0.0'))
    updated = Column(INTEGER(10), index=True)
    pokemon_id = Column(INTEGER(11))
    pokemon_form = Column(SMALLINT(6))
    pokemon_avg = Column(Float(asdecimal=True))
    pokemon_ratio = Column(Float(asdecimal=True), server_default=text('0'))
    pokemon_count = Column(Float(asdecimal=True), server_default=text('0'))
    nest_submitted_by = Column(String(200))
    area_name = Column(String(250))
    polygon_wkb = Column(Geometry(), nullable=False)
