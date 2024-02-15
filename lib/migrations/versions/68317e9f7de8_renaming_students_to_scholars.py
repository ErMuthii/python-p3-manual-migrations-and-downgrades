"""Renaming students to scholars

Revision ID: 68317e9f7de8
Revises: 791279dd0760
Create Date: 2024-02-15 15:41:38.216529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68317e9f7de8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')
