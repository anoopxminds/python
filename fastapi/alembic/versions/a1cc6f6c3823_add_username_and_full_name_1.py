"""add username and full_name #1

Revision ID: a1cc6f6c3823
Revises: d03850d72d66
Create Date: 2024-05-28 13:21:16.889980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1cc6f6c3823'
down_revision: Union[str, None] = 'd03850d72d66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
