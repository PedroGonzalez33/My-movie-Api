from pydantic import BaseModel, Field
from typing import Optional
import datetime

class Movie(BaseModel):
    ids:Optional[int] = None
    title: str = Field(min_length = 2, max_length = 15)
    overview: str = Field(max_length = 100, min_length = 2)
    year: int = Field(gt = 1900, le = datetime.date.today().year)
    rating: float = Field(gt = 0.0, le = 10.0)
    category: str = Field(max_length = 10, min_length = 5)

    class Config():
        schema_extra = {
            "example": {
                'ids': 1,
                'title': 'Movie Title', 
                'overview': 'Overview of the Movie', 
                'year': 2023,
                'rating': 10.0,
                'category': 'Category of the Movie'
            }
        }