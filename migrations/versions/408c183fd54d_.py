"""empty message

Revision ID: 408c183fd54d
Revises: 
Create Date: 2024-05-24 20:16:41.104864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '408c183fd54d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('fki_id_user', table_name='orders')
    op.drop_table('orders')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id_user', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('avg_order_complete_time', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('avg_day_orders', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('district', postgresql.ARRAY(sa.TEXT()), autoincrement=False, nullable=True),
    sa.Column('active_order', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), autoincrement=False, nullable=False),
    sa.Column('avg_list_time', postgresql.ARRAY(sa.TEXT()), autoincrement=False, nullable=True),
    sa.Column('time_start', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time_end', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('counter_ord', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time_start_work', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_user', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('orders',
    sa.Column('id_order', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('district', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_user', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], name='id_user'),
    sa.PrimaryKeyConstraint('id_order', name='orders_pkey')
    )
    op.create_index('fki_id_user', 'orders', ['id_user'], unique=False)
    # ### end Alembic commands ###