from pydantic import BaseModel, Field, field_validator



class BookCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=255,
        description="Название книги",
    )
    author: str = Field(
        min_length=1,
        max_length=40,
        description="Автор книги",
    )


    @classmethod
    @field_validator("title", "author")
    def validate_not_empty(cls, value: str) -> str:
        value = value.strip() # strip убирает пробелы по краям

        if not value:
            raise ValueError("Поле не может быть пустым")

        return value




class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    
    
