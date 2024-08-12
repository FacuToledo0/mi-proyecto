"""Creacion Modelo

Revision ID: 2719348e9e83
Revises: b68674155a30
Create Date: 2024-08-08 18:14:25.094942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2719348e9e83'
down_revision = 'b68674155a30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('modelo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('modelo')
    # ### end Alembic commands ###
