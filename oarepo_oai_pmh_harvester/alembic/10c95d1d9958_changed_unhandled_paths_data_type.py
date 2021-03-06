#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Changed unhandled paths data type"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '10c95d1d9958'
down_revision = '93118e4ff5b6'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oarepo_oai_provider', sa.Column('unhandled_paths', sa.JSON().with_variant(
        sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('oarepo_oai_provider', 'unhandled_paths')
    # ### end Alembic commands ###
