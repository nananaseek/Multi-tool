from fastapi import APIRouter

from app.applications.media_type.file_type import audio_type, \
    video_type, \
    photo_type
    
    

router = APIRouter()


@router.get("/audio", status_code=200, tags=['Media type'])
def get_audio_type():
    return audio_type

@router.get("/video", status_code=200, tags=['Media type'])
def get_video_type():
    return video_type

@router.get("/image", status_code=200, tags=['Media type'])
def get_image_type():
    return photo_type
