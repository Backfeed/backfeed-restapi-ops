"""empty message

Revision ID: dcc2f0c58b99
Revises: 
Create Date: 2016-04-26 16:01:57.709587

"""

# revision identifiers, used by Alembic.
revision = 'dcc2f0c58b99'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contract', 'time',
               existing_type=sa.DATETIME(),
               )
    op.alter_column('contribution', 'contract_id',
               existing_type=sa.INTEGER(),
               )
    op.alter_column('contribution', 'max_score',
               existing_type=sa.REAL(),
               )
    op.alter_column('contribution', 'time',
               existing_type=sa.DATETIME(),
               )
    op.alter_column('contribution', 'user_id',
               existing_type=sa.INTEGER(),
               )
    # op.drop_index('contribution_contract_id', table_name='contribution')
    # op.drop_index('contribution_user_id', table_name='contribution')
    op.alter_column('evaluation', 'contract_id',
               existing_type=sa.INTEGER(),
               )
    op.alter_column('evaluation', 'contribution_id',
               existing_type=sa.INTEGER(),
               )
    op.alter_column('evaluation', 'time',
               existing_type=sa.DATETIME(),
               )
    op.alter_column('evaluation', 'user_id',
               existing_type=sa.INTEGER(),
               )
    op.alter_column('evaluation', 'value',
               existing_type=sa.REAL(),
               )
    # op.drop_index('evaluation_contract_id', table_name='evaluation')
    # op.drop_index('evaluation_contribution_id', table_name='evaluation')
    # op.drop_index('evaluation_user_id', table_name='evaluation')
    # op.drop_column('evaluation', 'contribution_type')
    op.alter_column('user', 'contract_id',
               existing_type=sa.INTEGER(),
               )
    op.alter_column('user', 'reputation',
               existing_type=sa.REAL(),
               )
    op.alter_column('user', 'time',
               existing_type=sa.DATETIME(),
               )
    op.alter_column('user', 'tokens',
               existing_type=sa.REAL(),
               )
    # op.drop_index('user_contract_id', table_name='user')
    # op.create_unique_constraint(None, 'user', ['name'])
    # op.create_foreign_key(None, 'user', 'user', ['referrer_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('user_contract_id', 'user', ['contract_id'], unique=False)
    op.alter_column('user', 'tokens',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('user', 'time',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('user', 'reputation',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('user', 'contract_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('evaluation', sa.Column('contribution_type', sa.VARCHAR(length=255), nullable=True))
    op.create_index('evaluation_user_id', 'evaluation', ['user_id'], unique=False)
    op.create_index('evaluation_contribution_id', 'evaluation', ['contribution_id'], unique=False)
    op.create_index('evaluation_contract_id', 'evaluation', ['contract_id'], unique=False)
    op.alter_column('evaluation', 'value',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('evaluation', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('evaluation', 'time',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('evaluation', 'contribution_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('evaluation', 'contract_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('contribution_user_id', 'contribution', ['user_id'], unique=False)
    op.create_index('contribution_contract_id', 'contribution', ['contract_id'], unique=False)
    op.alter_column('contribution', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('contribution', 'time',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('contribution', 'max_score',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('contribution', 'contract_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('contract', 'time',
               existing_type=sa.DATETIME(),
               nullable=False)
    ### end Alembic commands ###
