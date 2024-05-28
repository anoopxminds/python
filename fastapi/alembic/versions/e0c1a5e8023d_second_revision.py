"""second revision

Revision ID: e0c1a5e8023d
Revises: 2b94d0de6e5d
Create Date: 2024-05-27 18:07:20.712123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0c1a5e8023d'
down_revision: Union[str, None] = '2b94d0de6e5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
