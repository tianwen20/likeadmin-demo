import os

from fastapi import APIRouter, UploadFile, Form

from work.http_base import unified_resp
from work.plugins.storage.storage_driver import StorageDriver

router = APIRouter(prefix='/upload')


@router.post('/image')
@unified_resp
async def upload_image(file: UploadFile, dir: str = Form(default='')):
    """上传图片"""
    folder = 'image'
    if dir:
        folder = os.path.join(folder, dir)
    res = await StorageDriver.upload(file, folder, 10)
    return res
