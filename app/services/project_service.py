from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:

    @staticmethod
    def create_project(db: Session, project: ProjectCreate, created_by: str):

        db_project = Project(
            project_name=project.project_name,
            project_code=project.project_code,
            description=project.description,
            environment=project.environment,
            status=project.status,
            organization_id=project.organization_id,
            created_by=created_by
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)

        return db_project

    @staticmethod
    def get_projects(db: Session):
        return db.query(Project).all()

    @staticmethod
    def get_project(db: Session, project_id: int):
        return db.query(Project).filter(Project.id == project_id).first()

    @staticmethod
    def delete_project(db: Session, project_id: int):

        project = db.query(Project).filter(Project.id == project_id).first()

        if not project:
            return None

        db.delete(project)
        db.commit()

        return project
