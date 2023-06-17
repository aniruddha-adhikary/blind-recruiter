from pydantic import BaseModel, Field
from typing import List

class Experience(BaseModel):
    title: str = Field(description="Job title")
    organization: str = Field(description="Organization name")
    start_date: str = Field(description="Start date")
    end_date: str = Field(description="End date")
    description: str = Field(description="Job description")

class Education(BaseModel):
    credential_name: str = Field(description="Credential name")
    institution_name: str = Field(description="Institution name")
    start_date: str = Field(description="Start date")
    end_date: str = Field(description="End date")
    description: str = Field(description="Education description")

class ParsedResume(BaseModel):
    github_url: str = Field(description="Github Profile URL")
    linkedin_url: str = Field(description="Linkedin Profile URL")
    experiences: List[Experience] = Field(description="List of experiences")
    education_history: List[Education] = Field(description="List of education history")
