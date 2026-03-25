from typing import TYPE_CHECKING
from core.models import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from core.models import User

class Role(Base):
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    
    user: Mapped['User'] = relationship(
        'role'
    )