from crud.base_crud import CRUDBase
from model.dataset import Dataset, DatasetType
from sqlmodel import Session
from typing import Optional
import uuid
from datetime import datetime


class CRUDDataset(CRUDBase[Dataset]):

    def create_dataset(
            self,
            tenant_id: str,
            user_id: str,
            dataset_name: str,
            desc: str,
            dataset_type: DatasetType,
            db_session: Session
    ) -> Optional[Dataset]:
        db_session = db_session or self.get_db_session()
        _dataset = Dataset(
            tenant_id=tenant_id,
            user_id=user_id,
            dataset_id=uuid.uuid4(),
            dataset_name=dataset_name,
            desc=desc,
            dataset_type=dataset_type,
            created_at=datetime.now(),
        )

        db_session.add(_dataset)
        db_session.commit()
        return _dataset


dataset = CRUDDataset(Dataset)
