#!/usr/bin/python3
"""SQLAlchemy ORM refactor of the procedural database example."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class User(Base):
    """Represent a user stored in the users table."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Return a useful string representation."""
        return "<User(id={}, username='{}', email='{}')>".format(
            self.id,
            self.username,
            self.email
        )


class UserManager:
    """Encapsulate ORM operations for the User model."""

    def __init__(self, session):
        """Initialize the manager with a SQLAlchemy Session."""
        self.session = session

    def create_user(self, username, email):
        """Create and add a new User using the ORM Session."""
        if not username or not email:
            print("Username and email are required.")
            return None

        try:
            new_user = User(username=username, email=email)
            self.session.add(new_user)
            self.session.commit()
            print("User '{}' created successfully.".format(username))
            return new_user
        except SQLAlchemyError as error:
            self.session.rollback()
            print("Error creating user: {}".format(error))
            return None

    def get_user_by_username(self, username):
        """Query for a User by username using the ORM Session."""
        user = self.session.query(User).filter(
            User.username == username
        ).first()

        if user:
            print("User found:", user)
        else:
            print("No user found with that username.")

        return user

    def update_user_email(self, username, new_email):
        """Update a user's email through the ORM object."""
        user = self.get_user_by_username(username)

        if user:
            user.email = new_email
            self.session.commit()
            print(
                "Email for '{}' updated to '{}'.".format(
                    username,
                    new_email
                )
            )
        else:
            print("No user found to update.")

    def delete_user(self, username):
        """Delete a user through the ORM Session."""
        user = self.get_user_by_username(username)

        if user:
            self.session.delete(user)
            self.session.commit()
            print("User '{}' deleted.".format(username))
        else:
            print("No user found to delete.")

    def list_users(self, limit=5):
        """Query and list users."""
        users = (
            self.session.query(User)
            .order_by(User.created_at.desc())
            .limit(limit)
            .all()
        )

        for user in users:
            print(user)

        return users


def main():
    """Demonstrate the SQLAlchemy ORM workflow."""
    engine = create_engine("sqlite:///:memory:", echo=False)

    Base.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        manager = UserManager(session)

        print("--- Creating Users ---")
        manager.create_user("alice_smith", "alice@example.com")
        manager.create_user("bob_jones", "bob@example.com")

        print("\n--- Querying User ---")
        manager.get_user_by_username("alice_smith")

        print("\n--- Updating User ---")
        manager.update_user_email(
            "alice_smith",
            "alice.smith@newdomain.com"
        )

        print("\n--- Listing Users ---")
        manager.list_users()

        print("\n--- Deleting User ---")
        manager.delete_user("bob_jones")
        manager.list_users()


if __name__ == "__main__":
    main()
