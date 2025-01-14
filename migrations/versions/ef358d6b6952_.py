"""empty message

Revision ID: ef358d6b6952
Revises: c2dd9a057882
Create Date: 2023-05-29 17:30:15.226234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef358d6b6952'
down_revision = 'c2dd9a057882'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('birth_year', sa.String(length=250), nullable=False),
    sa.Column('eye_color', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.Column('hair_color', sa.String(length=250), nullable=False),
    sa.Column('height', sa.String(length=250), nullable=False),
    sa.Column('films', sa.String(length=250), nullable=False),
    sa.Column('mass', sa.String(length=250), nullable=False),
    sa.Column('skin_color', sa.String(length=250), nullable=False),
    sa.Column('species', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('vehicles', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    # ### end Alembic commands ###
