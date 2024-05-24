from crud.base_crud import CRUDBase
from sqlmodel import Session, select
from typing import Optional
import uuid
from datetime import datetime
from model.dataset import DatasetBase, Dataset


class CRUDDataset(CRUDBase[Dataset]):

    def create_dataset(
            self,
            tenant_id: str,
            user_id: str,
            dataset_base: DatasetBase,
            db_session: Session
    ) -> Optional[Dataset]:
        db_session = db_session or self.get_db_session()
        _dataset = Dataset(
            tenant_id=tenant_id,
            user_id=user_id,
            dataset_id=uuid.uuid4(),
            dataset_name=dataset_base.dataset_name,
            desc=dataset_base.desc,
            dataset_type=dataset_base.dataset_type,
            created_at=datetime.now(),
        )

        db_session.add(_dataset)
        db_session.commit()
        return _dataset

    def get_by_id(
            self,
            db_session: Session,
            tenant_id: str,
            user_id: str,
            dataset_id: str
    ) -> Optional[Dataset]:
        db_session = db_session or self.get_db_session()

        query = select(self.model).where(
            self.model.tenant_id == tenant_id,
            self.model.user_id == user_id,
            self.model.dataset_id == dataset_id,
            self.model.deleted_at is None
        )

        return db_session.exec(query).one_or_none()

    def delete_by_id(
            self,
            db_session: Session,
            tenant_id: str,
            user_id: str,
            dataset_id: str
    ) -> bool:
        ds = self.get_by_id(db_session, tenant_id, user_id, dataset_id)
        if ds is None:
            return False

        ds.deleted_at = datetime.now()

        db_session.add(ds)
        db_session.commit()
        return True


dataset = CRUDDataset(Dataset)
