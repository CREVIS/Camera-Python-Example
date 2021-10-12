import os
import ctypes
import sys
from ctypes import POINTER

#Hook Function Event
EVENT_NEW_IMAGE				    = 0
EVENT_GRAB_ERROR			        = 1

# GC_ERROR redefine
MCAM_ERR_SUCCESS					= 0
MCAM_ERR_ERROR               		= -1001
MCAM_ERR_NOT_INITIALIZED     		= -1002
MCAM_ERR_NOT_IMPLEMENTED     		= -1003
MCAM_ERR_RESOURCE_IN_USE     		= -1004
MCAM_ERR_ACCESS_DENIED       		= -1005
MCAM_ERR_INVALID_HANDLE      		= -1006
MCAM_ERR_INVALID_ID          		= -1007
MCAM_ERR_NO_DATA             		= -1008
MCAM_ERR_INVALID_PARAMETER   		= -1009
MCAM_ERR_IO                  		= -1010
MCAM_ERR_TIMEOUT             		= -1011
MCAM_ERR_ABORT               		= -1012
MCAM_ERR_INVALID_BUFFER      		= -1013
MCAM_ERR_NOT_AVAILABLE       		= -1014

# Add Error type
MCAM_ERR_NOT_OPEN_DEVICE			= -10000
MCAM_ERR_NO_DEVICE				= -10001
MCAM_ERR_RESOURCE_USED				= -10002
MCAM_ERR_NO_SYSTEM				= -10003
MCAM_ERR_NOT_OPEN_SYSTEM			= -10004
MCAM_ERR_INVALID_BUFFER_SIZE		= -10005
MCAM_ERR_XML_PARSE				= -10006
MCAM_ERR_EXTERNAL_LOAD_LIBRARY		= -10007

#DeviceInfo
MCAM_DEVICEINFO_USER_ID			= 10000
MCAM_DEVICEINFO_MODEL_NAME			= 10001
MCAM_DEVICEINFO_SERIAL_NUMBER		= 10002
MCAM_DEVICEINFO_DEVICE_VERSION		= 10003
MCAM_DEVICEINFO_MAC_ADDRESS		= 10004
MCAM_DEVICEINFO_IP_ADDRESS			= 10005

#Continuous Grabbing Mode
MCAMU_CONTINUOUS_GRABBING_DISAABLE	= 0
MCAMU_CONTINUOUS_GRABBING_ENABLE	= 1

# Feature Name
MCAM_DEVICE_ID														 = b"DeviceID"
MCAM_DEVICE_VENDOR_NAME												 = b"DeviceVendorName"					# String
MCAM_DEVICE_MODEL_NAME													 = b"DeviceModelName"					# String
MCAM_DEVICE_MANUFACTURER_INFO											 = b"DeviceManufacturerInfo"				# String
MCAM_DEVICE_VERSION													 = b"DeviceVersion"						# String
MCAM_DEVICE_USER_ID													 = b"DeviceUserID"						# String
MCAM_DEVICE_SCANTYPE													 = b"DeviceScanType"						# Enumeration
MCAM_WIDTH															 = b"Width"			                    # Integer
MCAM_HEIGHT															 = b"Height"							# Integer
MCAM_PIXEL_FORMAT														 = b"PixelFormat"						# Enumeration
MCAM_WIDTH_MAX														 = b"WidthMax"							# Integer
MCAM_HEIGHT_MAX														 = b"HeightMax"							# Integer
MCAM_OFFSET_X															 = b"OffsetX"								# Integer
MCAM_OFFSET_Y															 = b"OffsetY"								# Integer
MCAM_BINNING_HORIZONTAL												 = b"BinningHorizontal"						# Integer
MCAM_BINNING_VERTICAL													 = b"BinningVertical"						# Integer
MCAM_TEST_PATTERN														 = b"TestPattern"							# Enumeration
MCAM_ACQUISITION_START													 = b"AcquisitionStart"						# Command
MCAM_ACQUISITION_STOP													 = b"AcquisitionStop"						# Command
MCAM_ACQUISITION_MODE													 = b"AcquisitionMode"						# Enumeration
MCAM_ACQUISITION_FRAME_COUNT											 = b"AcquisitionFrameCount"					# Integer
MCAM_TRIGGER_SELECTOR													 = b"TriggerSelector"						# Enumeration
MCAM_TRIGGER_MODE														 = b"TriggerMode"							# Enumeration
MCAM_TRIGGER_SOURCE													 = b"TriggerSource"						# Enumeration
MCAM_TRIGGER_ACTIVATION												 = b"TriggerActivation"						# Enumeration
MCAM_TRIGGER_SOFTWARE													 = b"TriggerSoftware"						# Command
MCAM_TRIGGER_DELAY													 = b"TriggerDelay"							# Float
MCAM_EXPOSURE_MODE													 = b"ExposureMode"							# Enumeration
MCAM_EXPOSURE_AUTO													 = b"ExposureAuto"							# Enumeration
MCAM_EXPOSURE_TIME													 = b"ExposureTime"							# Float
MCAM_TRANSFER_DELAY													 = b"TransferDelay"						# Integer
MCAM_ACQUISITION_FRAMERATE_ENABLE										 = b"AcquisitionFrameRateEnable"				# Enumeration
MCAM_ACQUISITIONF_RAMERATE												 = b"AcquisitionFrameRate"					# Float
MCAM_AUTO_EXPOSURE_TARGET												 = b"AutoExposureTarget"					# Integer
MCAM_LINE_SELECTOR													 = b"LineSelector"							# Enumeration
MCAM_LINE_MODE														 = b"LineMode"								# Enumeration
MCAM_LINE_INVERTER													 = b"LineInverter"							# Boolean
MCAM_LINE_STATUS														 = b"LineStatus"							# Boolean
MCAM_LINE_SOURCE														 = b"LineSource"							# Enumeration
MCAM_USER_OUTPUT_SELECTOR												 = b"UserOutputSelector"					# Enumeration
MCAM_USER_OUTPUT_VALUE													 = b"UserOutputValue"						# Boolean
MCAM_TIMER_SELECTOR													 = b"TimerSelector"						# Enumeration
MCAM_TIMER_DURATION													 = b"TimerDuration"						# Float
MCAM_TIMER_DELAY														 = b"TimerDelay"							# Float
MCAM_GAIN_SELECTOR        											 = b"GainSelector"							# Enumeration
MCAM_GAIN_RAW             											 = b"GainRaw"								# Integer
MCAM_GAIN_AUTO            											 = b"GainAuto"								# Enumeration
MCAM_BLACK_LEVEL_SELECTOR  											 = b"BlackLevelSelector"					# Enumeration
MCAM_BLACK_LEVEL_RAW       											 = b"BlackLevelRaw"						# Integer
MCAM_BALANCE_RATIO_SELECTOR											 = b"BalanceRatioSelector"					# Enumeration
MCAM_BALANCE_RATIO        											 = b"BalanceRatio"							# Float
MCAM_BALANCE_WHITE_AUTO												 = b"BalanceWhiteAuto"						# Enumeration
MCAM_LUT_ENABLE														 = b"LUTEnable"							# Boolean
MCAM_LUT_INDEX														 = b"LUTIndex"								# Integer
MCAM_LUT_VALUE														 = b"LUTValue"								# Integer
MCAM_PAYLOAD_SIZE														 = b"PayloadSize"							# Integer
GEV_VERSION_MAJOR                        								 = b"GevVersionMajor"						# Integer
GEV_VERSION_MINOR                        								 = b"GevVersionMinor"						# Integer
GEV_DEVICE_MODE_IS_BIGENDIAN               								 = b"GevDeviceModeIsBigEndian"				# Boolean
GEV_DEVICE_MODE_CHARACTER_SET              								 = b"GevDeviceModeCharacterSet"				# Enumeration
GEV_INTERFACE_SELECTOR                   								 = b"GevInterfaceSelector"					# Integer
GEV_MAC_ADDRESS                          								 = b"GevMACAddress"						# Integer
GEV_SUPPORTED_OPTION_SELECTOR             								 = b"GevSupportedOptionSelector"				# Enumeration
GEV_SUPPORTED_OPTION                     								 = b"GevSupportedOption"					# Integer
GEV_CURRENT_IP_CONFIGURATION_LLA           								 = b"GevCurrentIPConfigurationLLA"			# Boolean
GEV_CURRENT_IP_CONFIGURATION_DHCP          								 = b"GevCurrentIPConfigurationDHCP"			# Boolean
GEV_CURRENT_IP_CONFIGURATION_PERSISTENT_IP								 = b"GevCurrentIPConfigurationPersistentIP"	# Boolean
GEV_CURRENT_IP_ADDRESS                    								 = b"GevCurrentIPAddress"					# Integer
GEV_CURRENT_SUBNETMASK                   								 = b"GevCurrentSubnetMask"					# Integer
GEV_CURRENT_DEFAULT_GATEWAY               								 = b"GevCurrentDefaultGateway"				# Integer
GEV_FIRST_URL                            								 = b"GevFirstURL"							# String
GEV_SECOND_URL                           								 = b"GevSecondURL"							# String
GEV_NUMBER_OF_INTERFACES                  								 = b"GevNumberOfInterfaces"					# Integer
GEV_PERSISTENT_IP_ADDRESS                 								 = b"GevPersistentIPAddress"				# Integer
GEV_PERSISTENT_SUBNETMASK                								 = b"GevPersistentSubnetMask"				# Integer
GEV_PERSISTENT_DEFAULT_GATEWAY            								 = b"GevPersistentDefaultGateway"			# Integer
GEV_MESSAGE_CHANNEL_COUNT                 								 = b"GevMessageChannelCount"				# Integer
GEV_STREAM_CHANNEL_COUNT                  								 = b"GevStreamChannelCount"					# Integer
GEV_TIME_STAMP_TICK_FREQUENCY              								 = b"GevTimestampTickFrequency"				# Integer
GEV_TIME_STAMP_CONTROL_LATCH               								 = b"GevTimestampControlLatch"				# Command
GEV_TIME_STAMP_CONTROL_RESET               								 = b"GevTimestampControlReset"				# Command
GEV_TIME_STAMP_VALUE                      								 = b"GevTimestampValue"						# Integer
GEV_HEARTBEAT_TIMEOUT                    								 = b"GevHeartbeatTimeout"					# Integer
GEV_GVCP_HEARTBEAT_DISABLE                								 = b"GevGVCPHeartbeatDisable"				# Boolean
GEV_CCP                                 								 = b"GevCCP"								# Enumeration
GEV_MCP_HOST_PORT                         							 = b"GevMCPHostPort"						# Integer
GEV_MCTT                                								 = b"GevMCTT"								# Integer
GEV_MCRC                                								 = b"GevMCRC"								# Integer
GEV_STREAM_CHANNEL_SELECTOR               								 = b"GevStreamChannelSelector"				# Integer
GEV_SCP_INTERFACE_INDEX                   								 = b"GevSCPInterfaceIndex"					# Integer
GEV_SCP_HOST_PORT                         							 = b"GevSCPHostPort"						# Integer
GEV_SCPS_FIRE_TEST_PACKET                  							 = b"GevSCPSFireTestPacket"					# Boolean
GEV_SCPS_DO_NOT_FRAGMENT                   							 = b"GevSCPSDoNotFragment"					# Boolean
GEV_SCPS_BIG_ENDIAN                       								 = b"GevSCPSBigEndian"						# Boolean
GEV_SCPS_PACKETSIZE                      								 = b"GevSCPSPacketSize"						# Integer
GEV_SCPD                                								 = b"GevSCPD"								# Integer
GEV_SCDA																 = b"GevSCDA"								# Integer
USER_SET_SELECTOR														 = b"UserSetSelector"						# Enumeration
USER_SET_LOAD															 = b"UserSetLoad"							# Command
USER_SET_SAVE															 = b"UserSetSave"							# Command
MCAM_COLOR_TRANS_FORMATION_ENABLE										 = b"ColorTransformationEnable"				# Boolean
MCAM_COLOR_TRANS_FORMATION_VALUE_SELECTOR								 = b"ColorTransformationValueSelector"		# Enumeration
MCAM_COLOR_TRANS_FORMATION_VALUE										 = b"ColorTransformationValue"				# Float
MCAM_DEVICE_FILTER_DRIVER_MODE											 = b"DeviceFilterDriverMode"				# Enumeration
MCAM_DEVICE_COMMAND_TIMEOUT											 = b"DeviceCommandTimeout"					# Integer
MCAM_DEVICE_COMMAND_RETRY_NUMBER										 = b"DeviceCommandRetryNumber"				# Integer
MCAM_DEVICE_STREAM_TIMEOUT												 = b"DeviceStreamTimeout"					# Integer
MCAM_DEVICE_MISSING_PACKET_RECEIVE										 = b"DeviceMissingPacketReceive"				# Enumeration
MCAM_DEVICE_PACKET_RESEND												 = b"DevicePacketResend"					# Boolean
MCAM_DEVICE_MAX_PACKET_RESEND_COUNT										 = b"DeviceMaxPacketResendCount"				# Integer
MCAM_DEVICE_FIND_MAX_PACKET_SIZE										 = b"DeviceFindMaxPacketSize"				# Command
MCAM_DEVICE_MAX_PACKET_SIZE											 = b"DeviceMaxPacketSize"					# Integer

# Enumeration Feature Entry
PIXEL_FORMAT_MONO8													 = b"Mono8"	
PIXEL_FORMAT_MONO10													 = b"Mono10"
PIXEL_FORMAT_MONO12													 = b"Mono12"
PIXEL_FORMAT_MONO14													 = b"Mono14"
PIXEL_FORMAT_MONO10PACKED												 = b"Mono10Packed"
PIXEL_FORMAT_MONO12PACKED												 = b"Mono12Packed"
PIXEL_FORMAT_BAYERBG8													 = b"BayerBG8"
PIXEL_FORMAT_BAYERBG10													 = b"BayerBG10"
PIXEL_FORMAT_BAYERBG12													 = b"BayerBG12"
PIXEL_FORMAT_BAYERBG10PACKED											 = b"BayerBG10Packed"
PIXEL_FORMAT_BAYERBG12PACKED											 = b"BayerBG12Packed"
PIXEL_FORMAT_BAYERRG8													 = b"BayerRG8"
PIXEL_FORMAT_BAYERRG10													 = b"BayerRG10"
PIXEL_FORMAT_BAYERRG12													 = b"BayerRG12"
PIXEL_FORMAT_BAYERRG10PACKED											 = b"BayerRG10Packed"
PIXEL_FORMAT_BAYERRG12PACKED											 = b"BayerRG12Packed"
PIXEL_FORMAT_BAYERGR8													 = b"BayerGR8"
PIXEL_FORMAT_BAYERGR10													 = b"BayerGR10"
PIXEL_FORMAT_BAYERGR12													 = b"BayerGR12"
PIXEL_FORMAT_BAYERGR10PACKED											 = b"BayerGR10Packed"
PIXEL_FORMAT_BAYERGR12PACKED											 = b"BayerGR12Packed"
PIXEL_FORMAT_BAYERGB8													 = b"BayerGB8"
PIXEL_FORMAT_BAYERGB10													 = b"BayerGB10"
PIXEL_FORMAT_BAYERGB12													 = b"BayerGB12"
PIXEL_FORMAT_BAYERGB10PACKED											 = b"BayerGB10Packed"
PIXEL_FORMAT_BAYERGB12PACKED											 = b"BayerGB12Packed"
PIXEL_FORMAT_YUV422PACKED												 = b"YUV422Packed"
PIXEL_FORMAT_RGB8PACKED												 = b"RGB8Packed"
PIXEL_FORMAT_BGR8PACKED												 = b"BGR8Packed"
TEST_PATTERN_OFF														 = b"Off"
TEST_PATTERN_GREY_HORIZONTAL_RAMP										 = b"GreyHorizontalRamp"
TEST_PATTERN_GREY_VERTICAL_RAMP											 = b"GreyVerticalRamp"
ACQUISITION_MODE_CONTINUOUS											 = b"Continuous"
ACQUISITION_MODE_SINGLE_FRAME											 = b"SingleFrame"
ACQUISITION_MODE_MULTI_FRAME											 = b"MultiFrame"
TRIGGER_SELECTOR_FRAME_START											 = b"FrameStart"
TRIGGER_MODE_OFF														 = b"Off"
TRIGGER_MODE_ON														 = b"On"
TRIGGER_SOURCE_LINE1 													 = b"Line1"
TRIGGER_SOURCE_SOFTWARE 												 = b"Software"
TRIGGER_ACTIVATION_RISING_EDGE    										 = b"RisingEdge"
TRIGGER_ACTIVATION_FALLING_EDGE    										 = b"FallingEdge"
TRIGGER_ACTIVATION_LEVEL_LOW    										 = b"LevelLow"
TRIGGER_ACTIVATION_LEVEL_HIGH    										 = b"LevelHigh"
EXPOSURE_MODE_TIMED    												 = b"Timed"
EXPOSURE_MODE_TRIGGER_WIDTH 											 = b"TriggerWidth"
EXPOSURE_AUTO_OFF														 = b"Off"
EXPOSURE_AUTO_ONCE													 = b"Once"
EXPOSURE_AUTO_CONTINUOUS												 = b"Continuous"
ACQUISITION_FRAMERATE_ENABLE_OFF										 = b"Off"
ACQUISITION_FRAMERATE_ENABLE_ON											 = b"On"
LINE_SELECTOR_LINE1													 = b"Line1"
LINE_SELECTOR_LINE2													 = b"Line2"
LINE_MODE_INPUT														 = b"Input"
LINE_MODE_OUTPUT														 = b"Output"
LINE_SOURCE_OFF														 = b"Off"
LINE_SOURCE_EXPOSURE_ACTIVE											 = b"ExposureActive"
LINE_SOURCE_TIMER_ACTIVE												 = b"TimerActive"
LINE_SOURCE_USER_OUTPUT_1												 = b"UserOutput1"
USER_OUTPUT_SELECTOR_USER_OUTPUT_1										 = b"UserOutput1"
TIMER_SELECTOR_TIMER_1													 = b"Timer1"
GAIN_SELECTOR_ALL														 = b"All"
GAIN_AUTO_OFF															 = b"Off"
GAIN_AUTO_ONCE														 = b"Once"
GAIN_AUTO_CONTINUOUS													 = b"Continuous"
BLACK_LEVEL_SELECTOR_ALL												 = b"All"
BALANCE_RATIO_SELECTOR_RED												 = b"Red"
BALANCE_RATIO_SELECTOR_GREEN											 = b"Green"
BALANCE_RATIO_SELECTOR_BLUE											 = b"Blue"
BALANCE_WHITE_AUTO_OFF													 = b"Off"
BALANCE_WHITE_AUTO_ONCE												 = b"Once"
BALANCE_WHITE_AUTO_CONTINUOUS											 = b"Continuous"
GEV_DEVICE_MODE_CHARACTER_SET_UTF8										 = b"UTF8"
GEV_SUPPORTED_OPTION_SELECTOR_USER_DEFINED_NAME							 = b"UserDefinedName"
GEV_SUPPORTED_OPTION_SELECTOR_SERIAL_NUMBER							     = b"SerialNumber"
GEV_SUPPORTED_OPTION_SELECTOR_HEART_BEAT_DISABLE						     = b"HeartbeatDisable"
GEV_SUPPORTED_OPTION_SELECTOR_LINK_SPEED								     = b"LinkSpeed"
GEV_SUPPORTED_OPTION_SELECTOR_CCP_APPLICATION_SOCKET					     = b"CCPApplicationSocket"
GEV_SUPPORTED_OPTION_SELECTOR_MANIFEST_TABLE							     = b"ManifestTable"
GEV_SUPPORTED_OPTION_SELECTOR_TEST_DATA								     = b"TestData"
GEV_SUPPORTED_OPTION_SELECTOR_DISCOVERY_ACK_DELAY						     = b"DiscoveryAckDelay"
GEV_SUPPORTED_OPTION_SELECTOR_DISCOVERY_ACK_DELAY_WRITABLE				     = b"DiscoveryAckDelayWritable"
GEV_SUPPORTED_OPTION_SELECTOR_EXTENDED_STATUS_CODES					     = b"ExtendedStatusCodes"
GEV_SUPPORTED_OPTION_SELECTOR_PRIMARY_APPLICATION_SWITCH_OVER			     = b"PrimaryApplicationSwitchover"
GEV_SUPPORTED_OPTION_SELECTOR_ACTION								     = b"Action"
GEV_SUPPORTED_OPTION_SELECTOR_PENDING_ACK							     = b"PendingAck"
GEV_SUPPORTED_OPTION_SELECTOR_EVENT_DATA								     = b"EventData"
GEV_SUPPORTED_OPTION_SELECTOR_EVENT									     = b"Event"
GEV_SUPPORTED_OPTION_SELECTOR_PACKET_RESEND							     = b"PacketResend"
GEV_SUPPORTED_OPTION_SELECTOR_WRITE_MEM								     = b"WriteMem"
GEV_SUPPORTED_OPTION_SELECTOR_COMMANDS_CONCATENATION					     = b"CommandsConcatenation"
GEV_SUPPORTED_OPTION_SELECTOR_IP_CONFIGURATION_LLA					     = b"IPConfigurationLLA"
GEV_SUPPORTED_OPTION_SELECTOR_IP_CONFIGURATION_DHCP					     = b"IPConfigurationDHCP"
GEV_SUPPORTED_OPTION_SELECTOR_IP_CONFIGURATION_PERSISTENT_IP			     = b"IPConfigurationPersistentIP"
GEV_SUPPORTED_OPTION_SELECTOR_STREAM_CHANNEL_SOURCE_SOCKET				     = b"StreamChannelSourceSocket"
GEV_SUPPORTED_OPTION_SELECTOR_MESSAGE_CHANNEL_SOURCE_SOCKET			     = b"MessageChannelSourceSocket"
GEV_SUPPORTED_OPTION_SELECTOR_STREAM_CHANNEL_0_BIG_AND_LITTLE_ENDIAN	     = b"StreamChannel0BigAndLittleEndian"
GEV_SUPPORTED_OPTION_SELECTOR_STREAM_CHANNEL_0_IP_REASSEMBLY			     = b"StreamChannel0IPReassembly"
GEV_SUPPORTED_OPTION_SELECTOR_STREAM_CHANNEL_0_UNCONDITIONAL_STREAMING	     = b"StreamChannel0UnconditionalStreaming"
GEV_SUPPORTED_OPTION_SELECTOR_STREAM_CHANNEL_0_EXTENDED_CHUNK_DATA		     = b"StreamChannel0ExtendedChunkData"
GEV_CCP_OPEN_ACCESS												     = b"OpenAccess"
GEV_CCP_EXCLUSIVE_ACCESS												 = b"ExclusiveAccess"
GEV_CCP_CONTROL_ACCESS													 = b"ControlAccess"
USER_SET_SELECTOR_DEFAULT												 = b"Default"
USER_SET_SELECTOR_USER_SET_1											 = b"UserSet1"
USER_SET_SELECTOR_USER_SET_2											 = b"UserSet2"
USER_SET_SELECTOR_USER_SET_3											 = b"UserSet3"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUEBYGP								 = b"HUEBYGP"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUEBYGN								 = b"HUEBYGN"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUEBYHP								 = b"HUEBYHP"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUEBYHN								 = b"HUEBYHN"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUERYGP								 = b"HUERYGP"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUERYGN								 = b"HUERYGN"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUERYHP								 = b"HUERYHP"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUERYHN								 = b"HUERYHN"
COLOR_TRANSFORMATION_VALUE_SELECTOR_HUECG								 = b"HUECG"
DEVICE_FILTER_DRIVER_MODE_OFF											 = b"Off"
DEVICE_FILTER_DRIVER_MODE_ON											 = b"On"
DEVICE_MISSING_PACKET_RECEIVE_OFF										 = b"Off"
DEVICE_MISSING_PACKET_RECEIVE_ON										 = b"On"


crevis_path = os.environ.get('CREVIS_CAM_ROOT')
path_1 = os.path.join(crevis_path,r'Cameras\MCam40\bin\x64')
path_2 = os.path.join(crevis_path,r'Cameras\MCam40\genicam\bin\Win64_x64')
sys.path.append(path_1)
sys.path.append(path_2)

VFG40 = ctypes.cdll.LoadLibrary('VirtualFG40.dll')
VFG40.ST_InitSystem.argtypes = []
VFG40.ST_InitSystem.restype = ctypes.c_int32

VFG40.ST_FreeSystem.argtypes = []
VFG40.ST_FreeSystem.restype = ctypes.c_int32

VFG40.ST_IsInitSystem.argtypes = [POINTER(ctypes.c_bool)]
VFG40.ST_IsInitSystem.restype = ctypes.c_int32

VFG40.ST_GetAvailableCameraNum.argtypes = [POINTER(ctypes.c_uint32)]
VFG40.ST_GetAvailableCameraNum.restype = ctypes.c_int32

VFG40.ST_UpdateDevice.argtypes = []
VFG40.ST_UpdateDevice.restype = ctypes.c_int32

VFG40.ST_GetEnumDeviceID.argtypes = [ctypes.c_uint32, ctypes.c_char_p, POINTER(ctypes.c_uint32)]
VFG40.ST_GetEnumDeviceID.restype = ctypes.c_int32

VFG40.ST_GetEnumDeviceInfo.argtypes = [ctypes.c_uint32, ctypes.c_int32, ctypes.c_char_p, POINTER(ctypes.c_uint32)]
VFG40.ST_GetEnumDeviceInfo.restype = ctypes.c_int32

########################################################################################################
VFG40.ST_OpenDevice.argtypes = [ctypes.c_uint32, POINTER(ctypes.c_int32), ctypes.c_bool]
VFG40.ST_OpenDevice.restype = ctypes.c_int32

VFG40.ST_IsOpenDevice.argtypes = [ctypes.c_int32, POINTER(ctypes.c_bool)]	
VFG40.ST_AcqStart.restype = ctypes.c_int32
			
VFG40.ST_CloseDevice.argtypes = [ctypes.c_int32]
VFG40.ST_AcqStart.restype = ctypes.c_int32

VFG40.ST_AcqStart.argtypes = [ctypes.c_int32]
VFG40.ST_AcqStart.restype = ctypes.c_int32

VFG40.ST_AcqStop.argtypes = [ctypes.c_int32]
VFG40.ST_AcqStop.restype = ctypes.c_int32

VFG40.ST_DoAbortGrab.argtypes = [ctypes.c_uint32]
VFG40.ST_DoAbortGrab.restype = ctypes.c_int32

VFG40.ST_SetAcqInvalidTime.argtypes = [ctypes.c_uint32, ctypes.c_uint32]	
VFG40.ST_SetAcqInvalidTime.restype = ctypes.c_int32

VFG40.ST_GetAcqInvalidTime.argtypes = [ctypes.c_uint32, POINTER(ctypes.c_uint32)]
VFG40.ST_GetAcqInvalidTime.restype = ctypes.c_int32

VFG40.ST_SetContinuousGrabbing.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
VFG40.ST_SetContinuousGrabbing.restype = ctypes.c_int32

VFG40.ST_GetContinuousGrabbing.argtypes = [ctypes.c_uint32, POINTER(ctypes.c_uint32)]
VFG40.ST_GetContinuousGrabbing.restype = ctypes.c_int32

VFG40.ST_SetGrabTimeout.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
VFG40.ST_SetGrabTimeout.restype = ctypes.c_int32

VFG40.ST_GetGrabTimeout.argtypes = [ctypes.c_uint32, POINTER(ctypes.c_uint32)]
VFG40.ST_GetGrabTimeout.restype = ctypes.c_int32

VFG40.ST_GrabStartAsync.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
VFG40.ST_GrabStartAsync.restype = ctypes.c_int32

VFG40.ST_GrabImage.argtypes = [ctypes.c_int32, ctypes.c_void_p, ctypes.c_uint32]
VFG40.ST_GrabImage.restype = ctypes.c_int32

VFG40.ST_GrabImageAsync.argtypes = [ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32]
VFG40.ST_GrabImageAsync.restype = ctypes.c_int32

VFG40.ST_GetImageAvailable.argtypes = [ctypes.c_uint32, POINTER(ctypes.c_uint32)]	
VFG40.ST_GetImageAvailable.restype = ctypes.c_int32

########################################################################################################
VFG40.ST_GetTotalPacketCount.argtypes = [ctypes.c_uint32, POINTER(ctypes.c_uint64), POINTER(ctypes.c_uint64)]
VFG40.ST_GetTotalPacketCount.restype = ctypes.c_int32

VFG40.ST_GetLastError.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
VFG40.ST_GetLastError.restype = ctypes.c_int32

VFG40.ST_GetLastErrorDescription.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
VFG40.ST_GetLastErrorDescription.restype = ctypes.c_int32

VFG40.ST_SetDetailedLog.argtypes = [ctypes.c_int32, ctypes.c_bool]
VFG40.ST_SetDetailedLog.restype = ctypes.c_int32

VFG40.ST_GetDetailedLog.argtypes = [ctypes.c_int32, POINTER(ctypes.c_bool)]
VFG40.ST_GetDetailedLog.restype = ctypes.c_int32

########################################################################################################
VFG40.ST_SetIntReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_uint32]
VFG40.ST_SetIntReg.restype = ctypes.c_int32

VFG40.ST_GetIntReg.argtypes = [ctypes.c_int32, ctypes.c_char_p, POINTER(ctypes.c_int32)] 
VFG40.ST_GetIntReg.restype = ctypes.c_int32

VFG40.ST_SetFloatReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_double]
VFG40.ST_SetFloatReg.restype = ctypes.c_int32

VFG40.ST_GetFloatReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, POINTER(ctypes.c_double)]
VFG40.ST_GetFloatReg.restype = ctypes.c_int32

VFG40.ST_SetBoolReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_bool]	
VFG40.ST_SetBoolReg.restype = ctypes.c_int32

VFG40.ST_GetBoolReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, POINTER(ctypes.c_bool)]
VFG40.ST_GetBoolReg.restype = ctypes.c_int32

VFG40.ST_SetEnumReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p]
VFG40.ST_SetEnumReg.restype = ctypes.c_int32

VFG40.ST_GetEnumReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p, POINTER(ctypes.c_uint32)]
VFG40.ST_GetEnumReg.restype = ctypes.c_int32

VFG40.ST_SetStrReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p]
VFG40.ST_SetStrReg.restype = ctypes.c_int32

VFG40.ST_GetStrReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p, POINTER(ctypes.c_uint32)]
VFG40.ST_GetStrReg.restype = ctypes.c_int32

VFG40.ST_SetCmdReg.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
VFG40.ST_SetCmdReg.restype = ctypes.c_int32

########################################################################################################
VFG40.ST_GetIntRegRange.argtypes = [ctypes.c_uint32, ctypes.c_char_p, POINTER(ctypes.c_int32), POINTER(ctypes.c_int32), POINTER(ctypes.c_int32)]
VFG40.ST_GetIntRegRange.restype = ctypes.c_int32

VFG40.ST_GetFloatRegRange.argtypes = [ctypes.c_int32, ctypes.c_char_p, POINTER(ctypes.c_double), POINTER(ctypes.c_double)]
VFG40.ST_GetFloatRegRange.restype = ctypes.c_int32

VFG40.ST_GetEnumEntrySize.argtypes = [ctypes.c_int32, ctypes.c_char_p, POINTER(ctypes.c_int32)]
VFG40.ST_GetEnumEntrySize.restype = ctypes.c_int32

VFG40.ST_GetEnumEntryIntValue.argtypes = [ctypes.c_int32, ctypes.c_char_p, ctypes.c_int32, POINTER(ctypes.c_int32)]
VFG40.ST_GetEnumEntryIntValue.restype = ctypes.c_int32

VFG40.ST_GetEnumEntryValue.argtypes = [ctypes.c_int32, ctypes.c_char_p, ctypes.c_int32, ctypes.c_char_p, POINTER(ctypes.c_uint32)]		
VFG40.ST_GetEnumEntryValue.restype = ctypes.c_int32

#for Callback Function
callback_type = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
VFG40.ST_SetCallbackFunction.argtypes = [ctypes.c_int32, ctypes.c_int32, callback_type, ctypes.c_void_p]
VFG40.ST_SetCallbackFunction.restype = ctypes.c_int32
