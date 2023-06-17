from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class Experience(BaseModel):
    title: Optional[str] = Field(description="Job title")
    organization: Optional[str] = Field(description="Organization name")
    start_date: Optional[date] = Field(description="Start date")
    end_date: Optional[date] = Field(description="End date (Null if current job)")
    achievements: List[str] = Field(description="List of achievements (Leave empty if none provided))")
    responsibilities: List[str] = Field(description="List of responsibilities (Leave empty if none provided)))")


class Education(BaseModel):
    credential_name: Optional[str] = Field(description="Credential name")
    institution_name: Optional[str] = Field(description="Institution name")
    start_date: Optional[date] = Field(description="Start date")
    end_date: Optional[date] = Field(description="End date")
    description: str = Field(description="Education description")


class Experiences(BaseModel):
    experiences: List[Experience] = Field(description="List of experiences")


class EducationHistory(BaseModel):
    education_history: List[Experience] = Field(
        description="List of education history")


class Skills(BaseModel):
    skills: List[str] = Field(
        description="List of skills (Programming Languages, Frameworks)")


class ProfileLinks(BaseModel):
    github_url: str = Field(description="Github Profile URL")
    linkedin_url: str = Field(description="Linkedin Profile URL")


class ParsedResume(Experiences, EducationHistory, ProfileLinks):
    pass
