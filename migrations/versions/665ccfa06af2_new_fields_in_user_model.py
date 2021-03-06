"""new fields in user model

Revision ID: 665ccfa06af2
Revises: 6bc1fb2ab9ce
Create Date: 2021-04-15 17:02:44.324994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '665ccfa06af2'
down_revision = '6bc1fb2ab9ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
