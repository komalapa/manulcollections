"""Fix collation

Revision ID: 83c4a51fd7d2
Revises: 0cabed83787d
Create Date: 2018-05-05 00:28:23.407528

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '83c4a51fd7d2'
down_revision = '0cabed83787d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('book', 'isbn',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.alter_column('book', 'note',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('book', 'orig_name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    op.drop_index('name', table_name='book')
    op.alter_column('composition', 'annotation',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('genre', 'desc',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('publisher', 'city',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.alter_column('publisher', 'url',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.alter_column('serie', 'desc',
               existing_type=mysql.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('serie', 'desc',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('publisher', 'url',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    op.alter_column('publisher', 'city',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    op.alter_column('genre', 'desc',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('composition', 'annotation',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.create_index('name', 'book', ['name'], unique=True)
    op.alter_column('book', 'orig_name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    op.alter_column('book', 'note',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('book', 'isbn',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###
