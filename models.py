from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from database import engine

class Base(DeclarativeBase):
    pass

class SessionModel(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str]
    location: Mapped[str]
    stakes: Mapped[str]
    buy_in: Mapped[float]
    cash_out: Mapped [float]

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database tables created!")