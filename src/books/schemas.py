from src.db.models import Book
from pydantic import BaseModel

class BookResponseModel(Book):
    pass

class BookCreateModel(BaseModel):
    title: str
    author: str
    isbn: str
    description: str
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "Python Cookbook",
                "author": "David Beazley",
                "isbn": "978-1-4493-6846-9",
                "description": "A comprehensive cookbook for Python developers."
            }
        }
    }