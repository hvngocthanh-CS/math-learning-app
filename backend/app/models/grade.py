import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base


class Grade(Base):
    __tablename__ = "grades"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    number = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    icon_url = Column(String, nullable=True)

    chapters = relationship("Chapter", back_populates="grade", order_by="Chapter.order")
