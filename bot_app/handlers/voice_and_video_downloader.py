from aiogram import types
from aiogram.dispatcher import FSMContext

from ..app import dp
from ..core.utils.file import download_and_send_voice_message, download_and_send_video_note
from ..states import VoiceAndVideo


@dp.message_handler(content_types=types.ContentTypes.VOICE, state=VoiceAndVideo.file_handler)
async def handle_voice_message(message: types.Message, state=FSMContext):
    voice = message.voice
    file_id = voice.file_id

    # Передача даних голосового повідомлення у функцію для скачування та відправки
    voice_to_user = await download_and_send_voice_message(file_id)
    
    await message.answer_audio(voice_to_user)
    
    await state.finish()


@dp.message_handler(content_types=types.ContentTypes.VIDEO_NOTE, state=VoiceAndVideo.file_handler)
async def handle_video_note(message: types.Message, state=FSMContext):
    video_note = message.video_note
    file_id = video_note.file_id

    video_note_to_user = await download_and_send_video_note(file_id=file_id)
    
    await message.answer_video(video_note_to_user)
    
    await state.finish()