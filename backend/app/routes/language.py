from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

@router.get("/language/{lang}")
def get_language(lang: str):
    try:
        file_path = os.path.join(os.path.dirname(__file__), f'../../languages/{lang}.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            language_data = json.load(file)
        return language_data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Language not found")
