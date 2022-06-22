"""keep datetime as string; rename users table as user_submissions

Revision ID: 3dd7d2b610b8
Revises: c4500ccc59c8
Create Date: 2022-06-22 12:25:34.337718

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3dd7d2b610b8'
down_revision = 'c4500ccc59c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_submissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=500), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('submission_dt', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('question_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('submission_dt', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('submission_status', postgresql.ENUM('Accepted', 'Failed', name='status'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], name='users_question_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.drop_table('user_submissions')
    # ### end Alembic commands ###
