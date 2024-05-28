"""add username and full_name again

Revision ID: d03850d72d66
Revises: 74ac21b65fc9
Create Date: 2024-05-28 13:19:18.559056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd03850d72d66'
down_revision: Union[str, None] = '74ac21b65fc9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
