"""alters table column

Revision ID: 71836c8069a6
Revises: d0556465415d
Create Date: 2024-07-29 16:03:34.614222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71836c8069a6'
down_revision = 'd0556465415d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_trips')
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(), nullable=False))
        batch_op.drop_column('country')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('location')

    op.create_table('_alembic_tmp_trips',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('total_miles', sa.INTEGER(), nullable=False),
    sa.Column('custom', sa.BOOLEAN(), nullable=True),
    sa.Column('image_path', sa.VARCHAR(), nullable=True),
    sa.Column('location', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_trips')
    )
    # ### end Alembic commands ###