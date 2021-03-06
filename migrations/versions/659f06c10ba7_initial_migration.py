"""initial migration

Revision ID: 659f06c10ba7
Revises: 
Create Date: 2021-10-03 09:55:08.471507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '659f06c10ba7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('container',
    sa.Column('container_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('container_id')
    )
    op.create_index(op.f('ix_container_name'), 'container', ['name'], unique=True)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('ingredient',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('container_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['container_id'], ['container.container_id'], ),
    sa.PrimaryKeyConstraint('ingredient_id')
    )
    op.create_index(op.f('ix_ingredient_name'), 'ingredient', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ingredient_name'), table_name='ingredient')
    op.drop_table('ingredient')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_container_name'), table_name='container')
    op.drop_table('container')
    # ### end Alembic commands ###
