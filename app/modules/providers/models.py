import sqlalchemy as db

from sqlalchemy.orm import relationship

from ...db.engine import Base
from ...db.base import BaseMixin

from ..associations.models import ProductProvider


class Provider(BaseMixin, Base):
    __tablename__ = 'base_providers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    phone_number = db.Column(db.String)
    email = db.Column(db.String)
    # TODO: Adicionar campo de responsavel, que é o contato de atendimento

    # User Foreign key
    created_by = db.Column(db.Integer, db.ForeignKey('base_users.id'), nullable=False)

    # Relationships
    user = relationship("User", lazy="select", back_populates="providers_created", uselist=False)
    products = relationship("Product", secondary=ProductProvider, back_populates="providers")
