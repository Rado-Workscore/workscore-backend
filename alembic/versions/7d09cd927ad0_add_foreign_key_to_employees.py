from alembic import op
import sqlalchemy as sa
from typing import Union ,Sequence # Ավելացնել սա


# revision identifiers, used by Alembic.
revision: str = 'your_revision_id'  # Replace with the new revision ID.
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    # Add customer_id column to employees table
    op.add_column('employees', sa.Column('customer_id', sa.VARCHAR(length=50), nullable=True))

    # Add foreign key constraint between employees.customer_id and customer_config.customer_id
    op.create_foreign_key(
        "fk_employees_customer_id",  # Foreign key name
        "employees",  # Table where we are adding FK
        ["customer_id"],  # Column in employees that will be FK
        "customer_config",  # The referenced table
        ["customer_id"]  # Column in customer_config that is the primary key
    )

def downgrade() -> None:
    """Downgrade schema."""
    # Remove foreign key constraint
    op.drop_constraint("fk_employees_customer_id", "employees", type_="foreignkey")

    # Remove customer_id column from employees table
    op.drop_column('employees', 'customer_id')
