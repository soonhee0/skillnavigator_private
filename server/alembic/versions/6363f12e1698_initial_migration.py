"""Initial migration

Revision ID: 6363f12e1698
Revises: b9bf7ebdb36e
Create Date: 2023-12-28 23:41:55.833468

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6363f12e1698'
down_revision: Union[str, None] = 'b9bf7ebdb36e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
