from typing import TYPE_CHECKING
from core.models import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

if TYPE_CHECKING:
    from core.models import Role

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_role: Mapped[int] = mapped_column(ForeignKey('roles.id'))
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    password: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    is_active: Mapped[bool] 
    
    role: Mapped['Role'] = relationship(
        back_populates='user'
    )
    