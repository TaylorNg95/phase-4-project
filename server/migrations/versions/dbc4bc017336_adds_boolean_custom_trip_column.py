"""adds Boolean custom trip column

Revision ID: dbc4bc017336
Revises: 705602de04fb
Create Date: 2024-07-27 10:24:14.903445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbc4bc017336'
down_revision = '705602de04fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('custom', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.drop_column('custom')

    # ### end Alembic commands ###
