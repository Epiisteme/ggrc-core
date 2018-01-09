# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>


"""Change custom notification field to text type

Revision ID: 11357eaaa6f7
Revises: 529e4f55c8ed
Create Date: 2015-01-23 21:28:37.046054

"""

# revision identifiers, used by Alembic.
revision = '11357eaaa6f7'
down_revision = '529e4f55c8ed'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workflows', 'notify_custom_message',
      type_=sa.Text(),
      existing_type=sa.String(length=250),
      nullable=True)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workflows', 'notify_custom_message',
      type_=sa.String(length=250),
      existing_type=sa.Text(),
      nullable=True)
