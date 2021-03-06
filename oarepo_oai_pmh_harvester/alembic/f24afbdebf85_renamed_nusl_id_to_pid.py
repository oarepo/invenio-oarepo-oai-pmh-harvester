#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Renamed nusl_id to pid"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f24afbdebf85'
down_revision = 'e1c97dd21f28'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oarepo_oai_record', sa.Column('pid', sa.String(), nullable=False))
    op.create_unique_constraint(op.f('uq_oarepo_oai_record_pid'), 'oarepo_oai_record', ['pid'])
    op.drop_constraint('uq_oarepo_oai_record_nusl_id', 'oarepo_oai_record', type_='unique')
    op.drop_column('oarepo_oai_record', 'nusl_id')
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oarepo_oai_record', sa.Column('nusl_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_unique_constraint('uq_oarepo_oai_record_nusl_id', 'oarepo_oai_record', ['nusl_id'])
    op.drop_constraint(op.f('uq_oarepo_oai_record_pid'), 'oarepo_oai_record', type_='unique')
    op.drop_column('oarepo_oai_record', 'pid')
    # ### end Alembic commands ###
