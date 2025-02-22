"""
短信发送
"""

from fastapi import APIRouter, Depends

from work.front.schemas.sms import SmsSendIn
from work.front.service.sms import ISmsSendService, SmsSendService
from work.http_base import unified_resp

router = APIRouter(prefix='/sms')


@router.post('/send')
@unified_resp
async def sms_send(sms_in: SmsSendIn, sms_service: ISmsSendService = Depends(SmsSendService)):
    """
    pass
    :param file_in:
    :return:
    """
    return await sms_service.send(sms_in)
