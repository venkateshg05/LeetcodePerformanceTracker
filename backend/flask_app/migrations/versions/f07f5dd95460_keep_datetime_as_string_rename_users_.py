"""keep datetime as string; rename users table

Revision ID: f07f5dd95460
Revises: c35b64032caa
Create Date: 2022-06-22 11:59:46.413276

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f07f5dd95460'
down_revision = 'c35b64032caa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_submissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=500), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('submission_dt', sa.String(length=500), nullable=False),
    sa.Column('submission_status', sa.Enum('Accepted', 'Failed', name='status'), nullable=True),
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