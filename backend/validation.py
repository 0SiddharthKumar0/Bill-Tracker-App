from pydantic import BaseModel, ValidationError
from typing import Optional

class UploadedFile(BaseModel):
    name: str
    type: str
    size: int

    @classmethod
    def validate_file(cls, file):
        # Streamlit file has .name and .type
        return cls(name=file.name, type=file.type, size=file.size)