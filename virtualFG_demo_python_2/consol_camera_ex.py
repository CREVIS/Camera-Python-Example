import sys
import os
import ctypes 
import numpy as np
import cv2
import time

# camera lib
from VirtualFG import *

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
        
        nDevice = ctypes.c_uint32(0)

        #카메라 넘버 체크
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

        status = VFG40.ST_GetIntReg(hDevice.value, MCAM_WIDTH, ctypes.byref(img_width))
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        status = VFG40.ST_GetIntReg(hDevice.value, MCAM_HEIGHT, ctypes.byref(img_height))
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')
        
        img_size = (img_width.value, img_height.value)

        #VFG40: ST_AcqStart
        status = VFG40.ST_AcqStart(hDevice.value)
        if(status != MCAM_ERR_SUCCESS):
            raise Exception(f'ErrCode: {status}')

        cv2.namedWindow('demo')

        size = img_size[0] * img_size[1]
        
        img = np.zeros((img_size[1], img_size[0]), np.uint8)
        size = ctypes.c_uint32(size)

        for i in range(99):
            if(cv2.waitKey(33) > 0):
                break

            #영상 이미지 수신함수
            VFG40.ST_GrabImage(hDevice.value, img.ctypes.data, size.value)
            #opencv display
            recv_image = cv2.resize(img, dsize=(500, 500))
            cv2.imshow('demo', recv_image)

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





if __name__ == '__main__':
    main()