"""init

Revision ID: 7f2f0b7d724c
Revises:
Create Date: 2026-03-25 16:19:09.205143

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "7f2f0b7d724c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("id_role", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=False),
        sa.Column("patronymic", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id_role"],
            ["roles.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("password"),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("roles")
