import config
import logging
from module.login import check_local_status
from comm.net import air_api,url


@url('/api/AirMemo/pc/logout')
def logout(username):
    result = check_local_status()
    return air_api().post(url,data=result)
