"""add table role

Revision ID: bda0718163d1
Revises: 5b77a65b05b3
Create Date: 2026-03-25 13:00:50.787636

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "bda0718163d1"
down_revision: Union[str, None] = "5b77a65b05b3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.add_column("users", sa.Column("id_role", sa.Integer(), nullable=False))
    op.create_foreign_key("users_id_role_fkey", "users", "roles", ["id_role"], ["id"])


def downgrade() -> None:
    op.drop_constraint("users_id_role_fkey", "users", type_="foreignkey")
    op.drop_column("users", "id_role")
    op.drop_table("roles")
