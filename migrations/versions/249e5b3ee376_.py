"""empty message

Revision ID: 249e5b3ee376
Revises: 
Create Date: 2020-06-06 10:56:57.601346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '249e5b3ee376'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guide',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('surname', sa.String(length=20), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('travel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('guide_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['guide_id'], ['guide.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('travel')
    op.drop_table('guide')
    # ### end Alembic commands ###
