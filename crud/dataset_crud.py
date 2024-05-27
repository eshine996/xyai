from crud.base_crud import CRUDBase
from sqlmodel import Session, select
from typing import Optional, List
import uuid
from datetime import datetime
from model.dataset import DatasetBase, Dataset, DatasetPublic, DatasetBackend
from uuid import UUID


class CRUDDataset(CRUDBase[Dataset]):

    def create_dataset(
            self,
            tenant_id: UUID,
            user_id: UUID,
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
            backend=DatasetBackend.Backend_XiaoYang
        )

        db_session.add(_dataset)
        db_session.commit()
        return _dataset

    def get_by_id(
            self,
            db_session: Session,
            tenant_id: UUID,
            user_id: UUID,
            dataset_id: UUID
    ) -> Optional[Dataset]:
        db_session = db_session or self.get_db_session()

        query = select(self.model).where(
            self.model.tenant_id == tenant_id,
            self.model.user_id == user_id,
            self.model.dataset_id == dataset_id,
            self.model.deleted_at.is_(None)
        )

        return db_session.exec(query).one_or_none()

    def delete_by_id(
            self,
            db_session: Session,
            tenant_id: UUID,
            user_id: UUID,
            dataset_id: UUID
    ) -> bool:
        ds = self.get_by_id(db_session, tenant_id, user_id, dataset_id)
        if ds is None:
            return False

        ds.deleted_at = datetime.now()

        db_session.add(ds)
        db_session.commit()
        return True

    def update(
            self,
            db_session: Session,
            tenant_id: UUID,
            user_id: UUID,
            dataset_public: DatasetPublic
    ) -> bool:
        ds = self.get_by_id(
            db_session=db_session,
            tenant_id=tenant_id,
            user_id=user_id,
            dataset_id=dataset_public.dataset_id
        )
        if ds is None:
            return False

        if dataset_public.dataset_name:
            ds.dataset_name = dataset_public.dataset_name
        if dataset_public.desc:
            ds.desc = dataset_public.desc
        if dataset_public.dataset_type:
            ds.dataset_type = dataset_public.dataset_type

        db_session.add(ds)
        db_session.commit()

        return True

    def get_list(
            self,
            db_session: Session,
            tenant_id: UUID,
            user_id: UUID,
    ) -> List[DatasetPublic]:
        query = select(self.model).where(
            self.model.tenant_id == tenant_id,
            self.model.user_id == user_id,
            self.model.deleted_at.is_(None)
        )

        results = db_session.exec(query)

        return [
            DatasetPublic(
                dataset_id=ret.dataset_id,
                dataset_name=ret.dataset_name,
                desc=ret.desc,
                dataset_type=ret.dataset_type,
            ) for ret in results
        ]


dataset = CRUDDataset(Dataset)
