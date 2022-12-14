"""empty message

Revision ID: 4bb7ba59903c
Revises: 99761a78f3ca
Create Date: 2022-12-06 21:38:35.444511

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4bb7ba59903c'
down_revision = '99761a78f3ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=20), nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'profile_pic')
    # ### end Alembic commands ###
