from youmei.models.goods import Goods
from youmei.utils.db_migration import create_tables, drop_tables

__author__ = 'wly'

tables = [
    Goods,
]


def upgrade():
    create_tables(tables)


def downgrade():
    drop_tables(tables)


if __name__ == '__main__':
    upgrade()