from crud.base_crud import CRUDBase
from model import Tenant
from sqlmodel import Session
from typing import Optional
import uuid
from datetime import datetime


class CRUDTenant(CRUDBase[Tenant]):

    def create_tenant(self, tenant_name: str, db_session: Optional[Session] = None) -> Tenant:
        db_session = db_session or super().get_db_session()
        tenant_id = uuid.uuid4()
        _tenant = Tenant(
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            created_at=datetime.utcnow()
        )

        db_session.add(_tenant)
        db_session.commit()
        return _tenant


tenant = CRUDTenant(Tenant)
