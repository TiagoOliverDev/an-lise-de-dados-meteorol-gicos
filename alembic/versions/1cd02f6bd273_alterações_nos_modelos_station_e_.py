"""Alterações nos modelos Station e HistoricData

Revision ID: 1cd02f6bd273
Revises: 
Create Date: 2024-07-05 00:51:45.894442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cd02f6bd273'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('historic_data', 'value_data',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('stations', 'latitude',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('stations', 'longitude',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stations', 'longitude',
               existing_type=sa.String(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    op.alter_column('stations', 'latitude',
               existing_type=sa.String(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    op.alter_column('historic_data', 'value_data',
               existing_type=sa.String(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    # ### end Alembic commands ###
