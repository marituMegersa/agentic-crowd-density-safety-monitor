from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.crowd_density_safety_monitor.models import AgenticCrowdDensitySafetyMonitorSession, AgenticCrowdDensitySafetyMonitorItem
from app.domain.crowd_density_safety_monitor.schemas import AgenticCrowdDensitySafetyMonitorSessionCreate, AgenticCrowdDensitySafetyMonitorItemCreate

class AgenticCrowdDensitySafetyMonitorService:
    @staticmethod
    def create_session(db: Session, data: AgenticCrowdDensitySafetyMonitorSessionCreate) -> AgenticCrowdDensitySafetyMonitorSession:
        db_obj = AgenticCrowdDensitySafetyMonitorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticCrowdDensitySafetyMonitorSession:
        return db.query(AgenticCrowdDensitySafetyMonitorSession).filter(AgenticCrowdDensitySafetyMonitorSession.id == session_id).first()
