"""keep submission_status as string

Revision ID: d44f84369943
Revises: 3dd7d2b610b8
Create Date: 2022-06-22 12:27:10.023209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd44f84369943'
down_revision = '3dd7d2b610b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_submissions', sa.Column('submission_status', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_submissions', 'submission_status')
    # ### end Alembic commands ###
