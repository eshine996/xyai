from crud.base_crud import CRUDBase
from sqlmodel import Session, select, or_
from typing import List
from uuid import UUID
from model.agent import AgentPublic, Agent


class CRUDAgent(CRUDBase[Agent]):

    def get_agent_list(
            self,
            tenant_id: UUID,
            user_id: UUID,
            db_session: Session,
    ) -> List[AgentPublic]:
        db_session = db_session or self.get_db_session()
        query = select(self.model).where(
            self.model.tenant_id == tenant_id,
            self.model.deleted_at.is_(None),
            or_(
                self.model.is_public == 1,
                self.model.user_id == user_id,
            ),
        )

        results = db_session.exec(query)

        return [
            AgentPublic(
                agent_id=ret.agent_id,
                agent_name=ret.agent_name,
                desc=ret.desc,
                is_public=ret.is_public,
                category=ret.category,
                icon=ret.icon
            ) for ret in results
        ]


agent = CRUDAgent(Agent)
