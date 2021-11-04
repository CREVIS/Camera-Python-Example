import sys
import os
import ctypes 
import numpy as np
import cv2
import time

# camera lib
from VirtualFG import *


#전역
_img_size = None
_callfunc = None
_recv_img = None
_recv_img_flag = False

# camera grab시 call back
def on_GrabImgCallBack(Event, pImage, pUserDefine):
    try:
        global _recv_img
        global _recv_img_flag

        # void* array -> python Array
        pImage = ctypes.c_void_p(pImage) # void*
        size = _img_size[0] * _img_size[1]
        pBuffer = ctypes.POINTER((ctypes.c_uint8*size))
        buff = ctypes.cast(pImage, pBuffer) # 이미지를 버퍼로 캐스팅
        image = np.ctypeslib.as_array(buff.contents, size)   
        recv_image = np.reshape(image, newshape=(_img_size[1], _img_size[0]))
        
        #opencv display
        recv_image = cv2.resize(recv_image, dsize=(500, 500))
        _recv_img = recv_image
        _recv_img_flag = True

        return 0

    except Exception as err:
        #에러처리
        print(err.args[0])
        return -1

def main():
    try:
        #VFG40: VitualFG40 Init
        status = VFG40.ST_InitSystem()
        if(status != MCAM_ERR_SUCCESS):
                raise Exception(f'ErrCode: {status}')

        status = VFG40.ST_UpdateDevice()
        if(status != MCAM_ERR_SUCCESS):
                raise Exception(f'ErrCode: {status}')
        
        camNum = ctypes.c_uint(0)
        status = VFG40.ST_GetAvailableCameraNum(ctypes.byref(camNum))
        
        #camNum 가 1보다 작을때 종료
        if ( camNum.value < 1):
            print('Not found camera!')
            return

        hDevice = ctypes.c_int32(-1)

        #VFG40: Device Open
        status = VFG40.ST_OpenDevice(0, ctypes.byref(hDevice), 0)
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}, ErrMessage:VFG40.ST_OpenDevice')
        
        #VFG40: Camera Get Inform
        img_width = ctypes.c_int32(0)
        img_height = ctypes.c_int32(0)

        #VFG40: Triger Off
        status = VFG40.ST_SetEnumReg(hDevice.value, MCAM_TRIGGER_MODE, TRIGGER_MODE_OFF)
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        status = VFG40.ST_SetContinuousGrabbing(hDevice.value, MCAMU_CONTINUOUS_GRABBING_ENABLE)
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        status = VFG40.ST_GetIntReg(hDevice.value, MCAM_WIDTH, ctypes.byref(img_width))
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        status = VFG40.ST_GetIntReg(hDevice.value, MCAM_HEIGHT, ctypes.byref(img_height))
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')
        
        global _img_size
        _img_size = (img_width.value, img_height.value)

        # Grab 시 callback 함수 등록
        global _callfunc
        _callfunc = callback_type(on_GrabImgCallBack)
        status = VFG40.ST_SetCallbackFunction(hDevice, EVENT_NEW_IMAGE, _callfunc, ctypes.byref(ctypes.c_int32(0)))
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        cv2.namedWindow('demo')

        #VFG40: ST_AcqStart
        status = VFG40.ST_AcqStart(hDevice.value)
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        global _recv_img_flag
        global _recv_img

        while(1):
            if(_recv_img_flag is True):
                cv2.imshow('demo', _recv_img)
                _recv_img_flag = False

            if(cv2.waitKey(33) > 0):
                break

        #VFG40 ST_AcqStop
        status = VFG40.ST_AcqStop(hDevice.value)
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        cv2.destroyAllWindows()

        #free
        VFG40.ST_CloseDevice(hDevice.value)
        #hDevice 초기화
        hDevice = ctypes.c_int32(-1)    

         # virualfg free
        VFG40.ST_FreeSystem()

    except Exception as err:
        #에러처리
        #openDevice check
        if (hDevice.value < 0):
            return

        #free
        VFG40.ST_CloseDevice(hDevice.value)
        #hDevice 초기화
        hDevice = ctypes.c_int32(-1)  

         # virualfg free
        VFG40.ST_FreeSystem()
        return

# std
if __name__ == '__main__':
    main()