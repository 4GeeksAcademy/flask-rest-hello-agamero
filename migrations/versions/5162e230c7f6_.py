"""empty message

Revision ID: 5162e230c7f6
Revises: 44b558071098
Create Date: 2023-05-29 17:51:28.631288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5162e230c7f6'
down_revision = '44b558071098'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('starships_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'starships', ['starships_id'], ['id'])
        batch_op.create_foreign_key(None, 'homeworld', ['homeworld_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('starships_id')
        batch_op.drop_column('homeworld_id')

    # ### end Alembic commands ###
