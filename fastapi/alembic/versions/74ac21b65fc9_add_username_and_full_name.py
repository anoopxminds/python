"""add username and full_name

Revision ID: 74ac21b65fc9
Revises: d6fb75a23ed9
Create Date: 2024-05-28 13:14:20.307168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74ac21b65fc9'
down_revision: Union[str, None] = 'd6fb75a23ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
