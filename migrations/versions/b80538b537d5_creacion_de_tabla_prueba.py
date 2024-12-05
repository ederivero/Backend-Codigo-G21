"""creacion de tabla prueba

Revision ID: b80538b537d5
Revises: 04057f250220
Create Date: 2024-12-04 23:12:09.724144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80538b537d5'
down_revision = '04057f250220'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pruebas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pruebas')
    # ### end Alembic commands ###


def upgrade_postgres():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_postgres():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

