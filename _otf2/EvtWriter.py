
''' Generated by OTF2 Template Engine '''

import ctypes

from .Config import conf, StrParam
from .ErrorCodes import ErrorCode, HandleErrorCode
from .GeneralDefinitions import *
from .AttributeList import AttributeList
from .Definitions import *
from .Events import *


class EvtWriter(ctypes.Structure):
    pass

def EvtWriter_GetLocationID(writer, locationID = LocationRef()):
    c_GetLocationID = conf.lib.OTF2_EvtWriter_GetLocationID
    c_GetLocationID.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(LocationRef) ]
    c_GetLocationID.restype = ErrorCode
    c_GetLocationID.errcheck = HandleErrorCode
    c_GetLocationID(writer, ctypes.byref(locationID))
    return locationID.value

def EvtWriter_SetUserData(writer, userData):
    c_SetUserData = conf.lib.OTF2_EvtWriter_SetUserData
    c_SetUserData.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.py_object ]
    c_SetUserData.restype = ErrorCode
    c_SetUserData.errcheck = HandleErrorCode
    c_SetUserData(writer, ctypes.py_object(userData))

def EvtWriter_GetUserData(writer):
    c_GetUserData = conf.lib.OTF2_EvtWriter_GetUserData
    c_GetUserData.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(ctypes.c_void_p) ]
    c_GetUserData.restype = ErrorCode
    c_GetUserData.errcheck = HandleErrorCode
    userData = ctypes.c_void_p()
    c_GetUserData(writer, ctypes.byref(userData))
    return ctypes.cast(userData, ctypes.py_object).value

def EvtWriter_SetLocationID(writer, location):
    c_SetLocationID = conf.lib.OTF2_EvtWriter_SetLocationID
    c_SetLocationID.argtypes = [ ctypes.POINTER(EvtWriter), LocationRef]
    c_SetLocationID.restype = ErrorCode
    c_SetLocationID.errcheck = HandleErrorCode
    c_SetLocationID(writer, location)

def EvtWriter_GetNumberOfEvents(writer, numberOfEvents = ctypes.c_uint64()):
    c_GetNumberOfEvents = conf.lib.OTF2_EvtWriter_GetNumberOfEvents
    c_GetNumberOfEvents.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(ctypes.c_uint64)]
    c_GetNumberOfEvents.restype = ErrorCode
    c_GetNumberOfEvents.errcheck = HandleErrorCode
    c_GetNumberOfEvents(writer, ctypes.byref(numberOfEvents))
    return numberOfEvents.value

def EvtWriter_StoreRewindPoint(writer, rewindId):
    c_StoreRewindPoint = conf.lib.OTF2_EvtWriter_StoreRewindPoint
    c_StoreRewindPoint.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.c_uint32 ]
    c_StoreRewindPoint.restype = ErrorCode
    c_StoreRewindPoint.errcheck = HandleErrorCode
    c_StoreRewindPoint(writer, rewindId)

def EvtWriter_Rewind(writer, rewindId):
    c_Rewind = conf.lib.OTF2_EvtWriter_Rewind
    c_Rewind.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.c_uint32 ]
    c_Rewind.restype = ErrorCode
    c_Rewind.errcheck = HandleErrorCode
    c_Rewind(writer, rewindId)

def EvtWriter_ClearRewindPoint(writer, rewindId):
    c_ClearRewindPoint = conf.lib.OTF2_EvtWriter_ClearRewindPoint
    c_ClearRewindPoint.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.c_uint32 ]
    c_ClearRewindPoint.restype = ErrorCode
    c_ClearRewindPoint.errcheck = HandleErrorCode
    c_ClearRewindPoint(writer, rewindId)

def EvtWriter_BufferFlush(writer, attributeList, time, stopTime):
    c_BufferFlush = conf.lib.OTF2_EvtWriter_BufferFlush
    c_BufferFlush.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, TimeStamp ]
    c_BufferFlush.restype = ErrorCode
    c_BufferFlush.errcheck = HandleErrorCode
    c_BufferFlush(writer, attributeList, time, stopTime)

def EvtWriter_MeasurementOnOff(writer, attributeList, time, measurementMode):
    c_MeasurementOnOff = conf.lib.OTF2_EvtWriter_MeasurementOnOff
    c_MeasurementOnOff.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, MeasurementMode ]
    c_MeasurementOnOff.restype = ErrorCode
    c_MeasurementOnOff.errcheck = HandleErrorCode
    c_MeasurementOnOff(writer, attributeList, time, measurementMode)

def EvtWriter_Enter(writer, attributeList, time, region):
    c_Enter = conf.lib.OTF2_EvtWriter_Enter
    c_Enter.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RegionRef ]
    c_Enter.restype = ErrorCode
    c_Enter.errcheck = HandleErrorCode
    c_Enter(writer, attributeList, time, region)

def EvtWriter_Leave(writer, attributeList, time, region):
    c_Leave = conf.lib.OTF2_EvtWriter_Leave
    c_Leave.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RegionRef ]
    c_Leave.restype = ErrorCode
    c_Leave.errcheck = HandleErrorCode
    c_Leave(writer, attributeList, time, region)

def EvtWriter_MpiSend(writer, attributeList, time, receiver, communicator, msgTag, msgLength):
    c_MpiSend = conf.lib.OTF2_EvtWriter_MpiSend
    c_MpiSend.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint32, CommRef, ctypes.c_uint32, ctypes.c_uint64 ]
    c_MpiSend.restype = ErrorCode
    c_MpiSend.errcheck = HandleErrorCode
    c_MpiSend(writer, attributeList, time, receiver, communicator, msgTag, msgLength)

def EvtWriter_MpiIsend(writer, attributeList, time, receiver, communicator, msgTag, msgLength, requestID):
    c_MpiIsend = conf.lib.OTF2_EvtWriter_MpiIsend
    c_MpiIsend.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint32, CommRef, ctypes.c_uint32, ctypes.c_uint64, ctypes.c_uint64 ]
    c_MpiIsend.restype = ErrorCode
    c_MpiIsend.errcheck = HandleErrorCode
    c_MpiIsend(writer, attributeList, time, receiver, communicator, msgTag, msgLength, requestID)

def EvtWriter_MpiIsendComplete(writer, attributeList, time, requestID):
    c_MpiIsendComplete = conf.lib.OTF2_EvtWriter_MpiIsendComplete
    c_MpiIsendComplete.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint64 ]
    c_MpiIsendComplete.restype = ErrorCode
    c_MpiIsendComplete.errcheck = HandleErrorCode
    c_MpiIsendComplete(writer, attributeList, time, requestID)

def EvtWriter_MpiIrecvRequest(writer, attributeList, time, requestID):
    c_MpiIrecvRequest = conf.lib.OTF2_EvtWriter_MpiIrecvRequest
    c_MpiIrecvRequest.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint64 ]
    c_MpiIrecvRequest.restype = ErrorCode
    c_MpiIrecvRequest.errcheck = HandleErrorCode
    c_MpiIrecvRequest(writer, attributeList, time, requestID)

def EvtWriter_MpiRecv(writer, attributeList, time, sender, communicator, msgTag, msgLength):
    c_MpiRecv = conf.lib.OTF2_EvtWriter_MpiRecv
    c_MpiRecv.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint32, CommRef, ctypes.c_uint32, ctypes.c_uint64 ]
    c_MpiRecv.restype = ErrorCode
    c_MpiRecv.errcheck = HandleErrorCode
    c_MpiRecv(writer, attributeList, time, sender, communicator, msgTag, msgLength)

def EvtWriter_MpiIrecv(writer, attributeList, time, sender, communicator, msgTag, msgLength, requestID):
    c_MpiIrecv = conf.lib.OTF2_EvtWriter_MpiIrecv
    c_MpiIrecv.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint32, CommRef, ctypes.c_uint32, ctypes.c_uint64, ctypes.c_uint64 ]
    c_MpiIrecv.restype = ErrorCode
    c_MpiIrecv.errcheck = HandleErrorCode
    c_MpiIrecv(writer, attributeList, time, sender, communicator, msgTag, msgLength, requestID)

def EvtWriter_MpiRequestTest(writer, attributeList, time, requestID):
    c_MpiRequestTest = conf.lib.OTF2_EvtWriter_MpiRequestTest
    c_MpiRequestTest.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint64 ]
    c_MpiRequestTest.restype = ErrorCode
    c_MpiRequestTest.errcheck = HandleErrorCode
    c_MpiRequestTest(writer, attributeList, time, requestID)

def EvtWriter_MpiRequestCancelled(writer, attributeList, time, requestID):
    c_MpiRequestCancelled = conf.lib.OTF2_EvtWriter_MpiRequestCancelled
    c_MpiRequestCancelled.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint64 ]
    c_MpiRequestCancelled.restype = ErrorCode
    c_MpiRequestCancelled.errcheck = HandleErrorCode
    c_MpiRequestCancelled(writer, attributeList, time, requestID)

def EvtWriter_MpiCollectiveBegin(writer, attributeList, time):
    c_MpiCollectiveBegin = conf.lib.OTF2_EvtWriter_MpiCollectiveBegin
    c_MpiCollectiveBegin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp ]
    c_MpiCollectiveBegin.restype = ErrorCode
    c_MpiCollectiveBegin.errcheck = HandleErrorCode
    c_MpiCollectiveBegin(writer, attributeList, time)

def EvtWriter_MpiCollectiveEnd(writer, attributeList, time, collectiveOp, communicator, root, sizeSent, sizeReceived):
    c_MpiCollectiveEnd = conf.lib.OTF2_EvtWriter_MpiCollectiveEnd
    c_MpiCollectiveEnd.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CollectiveOp, CommRef, ctypes.c_uint32, ctypes.c_uint64, ctypes.c_uint64 ]
    c_MpiCollectiveEnd.restype = ErrorCode
    c_MpiCollectiveEnd.errcheck = HandleErrorCode
    c_MpiCollectiveEnd(writer, attributeList, time, collectiveOp, communicator, root, sizeSent, sizeReceived)

def EvtWriter_OmpFork(writer, attributeList, time, numberOfRequestedThreads):
    c_OmpFork = conf.lib.OTF2_EvtWriter_OmpFork
    c_OmpFork.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint32 ]
    c_OmpFork.restype = ErrorCode
    c_OmpFork.errcheck = HandleErrorCode
    c_OmpFork(writer, attributeList, time, numberOfRequestedThreads)

def EvtWriter_OmpJoin(writer, attributeList, time):
    c_OmpJoin = conf.lib.OTF2_EvtWriter_OmpJoin
    c_OmpJoin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp ]
    c_OmpJoin.restype = ErrorCode
    c_OmpJoin.errcheck = HandleErrorCode
    c_OmpJoin(writer, attributeList, time)

def EvtWriter_OmpAcquireLock(writer, attributeList, time, lockID, acquisitionOrder):
    c_OmpAcquireLock = conf.lib.OTF2_EvtWriter_OmpAcquireLock
    c_OmpAcquireLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint32, ctypes.c_uint32 ]
    c_OmpAcquireLock.restype = ErrorCode
    c_OmpAcquireLock.errcheck = HandleErrorCode
    c_OmpAcquireLock(writer, attributeList, time, lockID, acquisitionOrder)

def EvtWriter_OmpReleaseLock(writer, attributeList, time, lockID, acquisitionOrder):
    c_OmpReleaseLock = conf.lib.OTF2_EvtWriter_OmpReleaseLock
    c_OmpReleaseLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint32, ctypes.c_uint32 ]
    c_OmpReleaseLock.restype = ErrorCode
    c_OmpReleaseLock.errcheck = HandleErrorCode
    c_OmpReleaseLock(writer, attributeList, time, lockID, acquisitionOrder)

def EvtWriter_OmpTaskCreate(writer, attributeList, time, taskID):
    c_OmpTaskCreate = conf.lib.OTF2_EvtWriter_OmpTaskCreate
    c_OmpTaskCreate.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint64 ]
    c_OmpTaskCreate.restype = ErrorCode
    c_OmpTaskCreate.errcheck = HandleErrorCode
    c_OmpTaskCreate(writer, attributeList, time, taskID)

def EvtWriter_OmpTaskSwitch(writer, attributeList, time, taskID):
    c_OmpTaskSwitch = conf.lib.OTF2_EvtWriter_OmpTaskSwitch
    c_OmpTaskSwitch.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint64 ]
    c_OmpTaskSwitch.restype = ErrorCode
    c_OmpTaskSwitch.errcheck = HandleErrorCode
    c_OmpTaskSwitch(writer, attributeList, time, taskID)

def EvtWriter_OmpTaskComplete(writer, attributeList, time, taskID):
    c_OmpTaskComplete = conf.lib.OTF2_EvtWriter_OmpTaskComplete
    c_OmpTaskComplete.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_uint64 ]
    c_OmpTaskComplete.restype = ErrorCode
    c_OmpTaskComplete.errcheck = HandleErrorCode
    c_OmpTaskComplete(writer, attributeList, time, taskID)

def EvtWriter_Metric(writer, attributeList, time, metric, typeIDs, metricValues):
    numberOfMetrics = len(metricValues)
    assert(numberOfMetrics == len(typeIDs))

    TypeArrayType = Type * numberOfMetrics
    type_ids_list = TypeArrayType()
    type_ids_list[:] = typeIDs

    MetricValueArrayType = MetricValue * numberOfMetrics
    metric_values_list = MetricValueArrayType()
    metric_values_list[:] = metricValues

    c_Metric = conf.lib.OTF2_EvtWriter_Metric
    c_Metric.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, MetricRef, ctypes.c_uint8, TypeArrayType, MetricValueArrayType ]
    c_Metric.restype = ErrorCode
    c_Metric.errcheck = HandleErrorCode
    c_Metric(writer, attributeList, time , metric, numberOfMetrics, type_ids_list, metric_values_list)

def EvtWriter_ParameterString(writer, attributeList, time, parameter, string):
    c_ParameterString = conf.lib.OTF2_EvtWriter_ParameterString
    c_ParameterString.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ParameterRef, StringRef ]
    c_ParameterString.restype = ErrorCode
    c_ParameterString.errcheck = HandleErrorCode
    c_ParameterString(writer, attributeList, time, parameter, string)

def EvtWriter_ParameterInt(writer, attributeList, time, parameter, value):
    c_ParameterInt = conf.lib.OTF2_EvtWriter_ParameterInt
    c_ParameterInt.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ParameterRef, ctypes.c_int64 ]
    c_ParameterInt.restype = ErrorCode
    c_ParameterInt.errcheck = HandleErrorCode
    c_ParameterInt(writer, attributeList, time, parameter, value)

def EvtWriter_ParameterUnsignedInt(writer, attributeList, time, parameter, value):
    c_ParameterUnsignedInt = conf.lib.OTF2_EvtWriter_ParameterUnsignedInt
    c_ParameterUnsignedInt.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ParameterRef, ctypes.c_uint64 ]
    c_ParameterUnsignedInt.restype = ErrorCode
    c_ParameterUnsignedInt.errcheck = HandleErrorCode
    c_ParameterUnsignedInt(writer, attributeList, time, parameter, value)

def EvtWriter_RmaWinCreate(writer, attributeList, time, win):
    c_RmaWinCreate = conf.lib.OTF2_EvtWriter_RmaWinCreate
    c_RmaWinCreate.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef ]
    c_RmaWinCreate.restype = ErrorCode
    c_RmaWinCreate.errcheck = HandleErrorCode
    c_RmaWinCreate(writer, attributeList, time, win)

def EvtWriter_RmaWinDestroy(writer, attributeList, time, win):
    c_RmaWinDestroy = conf.lib.OTF2_EvtWriter_RmaWinDestroy
    c_RmaWinDestroy.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef ]
    c_RmaWinDestroy.restype = ErrorCode
    c_RmaWinDestroy.errcheck = HandleErrorCode
    c_RmaWinDestroy(writer, attributeList, time, win)

def EvtWriter_RmaCollectiveBegin(writer, attributeList, time):
    c_RmaCollectiveBegin = conf.lib.OTF2_EvtWriter_RmaCollectiveBegin
    c_RmaCollectiveBegin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp ]
    c_RmaCollectiveBegin.restype = ErrorCode
    c_RmaCollectiveBegin.errcheck = HandleErrorCode
    c_RmaCollectiveBegin(writer, attributeList, time)

def EvtWriter_RmaCollectiveEnd(writer, attributeList, time, collectiveOp, syncLevel, win, root, bytesSent, bytesReceived):
    c_RmaCollectiveEnd = conf.lib.OTF2_EvtWriter_RmaCollectiveEnd
    c_RmaCollectiveEnd.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CollectiveOp, RmaSyncLevel, RmaWinRef, ctypes.c_uint32, ctypes.c_uint64, ctypes.c_uint64 ]
    c_RmaCollectiveEnd.restype = ErrorCode
    c_RmaCollectiveEnd.errcheck = HandleErrorCode
    c_RmaCollectiveEnd(writer, attributeList, time, collectiveOp, syncLevel, win, root, bytesSent, bytesReceived)

def EvtWriter_RmaGroupSync(writer, attributeList, time, syncLevel, win, group):
    c_RmaGroupSync = conf.lib.OTF2_EvtWriter_RmaGroupSync
    c_RmaGroupSync.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaSyncLevel, RmaWinRef, GroupRef ]
    c_RmaGroupSync.restype = ErrorCode
    c_RmaGroupSync.errcheck = HandleErrorCode
    c_RmaGroupSync(writer, attributeList, time, syncLevel, win, group)

def EvtWriter_RmaRequestLock(writer, attributeList, time, win, remote, lockId, lockType):
    c_RmaRequestLock = conf.lib.OTF2_EvtWriter_RmaRequestLock
    c_RmaRequestLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, ctypes.c_uint64, LockType ]
    c_RmaRequestLock.restype = ErrorCode
    c_RmaRequestLock.errcheck = HandleErrorCode
    c_RmaRequestLock(writer, attributeList, time, win, remote, lockId, lockType)

def EvtWriter_RmaAcquireLock(writer, attributeList, time, win, remote, lockId, lockType):
    c_RmaAcquireLock = conf.lib.OTF2_EvtWriter_RmaAcquireLock
    c_RmaAcquireLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, ctypes.c_uint64, LockType ]
    c_RmaAcquireLock.restype = ErrorCode
    c_RmaAcquireLock.errcheck = HandleErrorCode
    c_RmaAcquireLock(writer, attributeList, time, win, remote, lockId, lockType)

def EvtWriter_RmaTryLock(writer, attributeList, time, win, remote, lockId, lockType):
    c_RmaTryLock = conf.lib.OTF2_EvtWriter_RmaTryLock
    c_RmaTryLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, ctypes.c_uint64, LockType ]
    c_RmaTryLock.restype = ErrorCode
    c_RmaTryLock.errcheck = HandleErrorCode
    c_RmaTryLock(writer, attributeList, time, win, remote, lockId, lockType)

def EvtWriter_RmaReleaseLock(writer, attributeList, time, win, remote, lockId):
    c_RmaReleaseLock = conf.lib.OTF2_EvtWriter_RmaReleaseLock
    c_RmaReleaseLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, ctypes.c_uint64 ]
    c_RmaReleaseLock.restype = ErrorCode
    c_RmaReleaseLock.errcheck = HandleErrorCode
    c_RmaReleaseLock(writer, attributeList, time, win, remote, lockId)

def EvtWriter_RmaSync(writer, attributeList, time, win, remote, syncType):
    c_RmaSync = conf.lib.OTF2_EvtWriter_RmaSync
    c_RmaSync.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, RmaSyncType ]
    c_RmaSync.restype = ErrorCode
    c_RmaSync.errcheck = HandleErrorCode
    c_RmaSync(writer, attributeList, time, win, remote, syncType)

def EvtWriter_RmaWaitChange(writer, attributeList, time, win):
    c_RmaWaitChange = conf.lib.OTF2_EvtWriter_RmaWaitChange
    c_RmaWaitChange.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef ]
    c_RmaWaitChange.restype = ErrorCode
    c_RmaWaitChange.errcheck = HandleErrorCode
    c_RmaWaitChange(writer, attributeList, time, win)

def EvtWriter_RmaPut(writer, attributeList, time, win, remote, bytes, matchingId):
    c_RmaPut = conf.lib.OTF2_EvtWriter_RmaPut
    c_RmaPut.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, ctypes.c_uint64, ctypes.c_uint64 ]
    c_RmaPut.restype = ErrorCode
    c_RmaPut.errcheck = HandleErrorCode
    c_RmaPut(writer, attributeList, time, win, remote, bytes, matchingId)

def EvtWriter_RmaGet(writer, attributeList, time, win, remote, bytes, matchingId):
    c_RmaGet = conf.lib.OTF2_EvtWriter_RmaGet
    c_RmaGet.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, ctypes.c_uint64, ctypes.c_uint64 ]
    c_RmaGet.restype = ErrorCode
    c_RmaGet.errcheck = HandleErrorCode
    c_RmaGet(writer, attributeList, time, win, remote, bytes, matchingId)

def EvtWriter_RmaAtomic(writer, attributeList, time, win, remote, type, bytesSent, bytesReceived, matchingId):
    c_RmaAtomic = conf.lib.OTF2_EvtWriter_RmaAtomic
    c_RmaAtomic.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint32, RmaAtomicType, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64 ]
    c_RmaAtomic.restype = ErrorCode
    c_RmaAtomic.errcheck = HandleErrorCode
    c_RmaAtomic(writer, attributeList, time, win, remote, type, bytesSent, bytesReceived, matchingId)

def EvtWriter_RmaOpCompleteBlocking(writer, attributeList, time, win, matchingId):
    c_RmaOpCompleteBlocking = conf.lib.OTF2_EvtWriter_RmaOpCompleteBlocking
    c_RmaOpCompleteBlocking.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint64 ]
    c_RmaOpCompleteBlocking.restype = ErrorCode
    c_RmaOpCompleteBlocking.errcheck = HandleErrorCode
    c_RmaOpCompleteBlocking(writer, attributeList, time, win, matchingId)

def EvtWriter_RmaOpCompleteNonBlocking(writer, attributeList, time, win, matchingId):
    c_RmaOpCompleteNonBlocking = conf.lib.OTF2_EvtWriter_RmaOpCompleteNonBlocking
    c_RmaOpCompleteNonBlocking.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint64 ]
    c_RmaOpCompleteNonBlocking.restype = ErrorCode
    c_RmaOpCompleteNonBlocking.errcheck = HandleErrorCode
    c_RmaOpCompleteNonBlocking(writer, attributeList, time, win, matchingId)

def EvtWriter_RmaOpTest(writer, attributeList, time, win, matchingId):
    c_RmaOpTest = conf.lib.OTF2_EvtWriter_RmaOpTest
    c_RmaOpTest.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint64 ]
    c_RmaOpTest.restype = ErrorCode
    c_RmaOpTest.errcheck = HandleErrorCode
    c_RmaOpTest(writer, attributeList, time, win, matchingId)

def EvtWriter_RmaOpCompleteRemote(writer, attributeList, time, win, matchingId):
    c_RmaOpCompleteRemote = conf.lib.OTF2_EvtWriter_RmaOpCompleteRemote
    c_RmaOpCompleteRemote.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, RmaWinRef, ctypes.c_uint64 ]
    c_RmaOpCompleteRemote.restype = ErrorCode
    c_RmaOpCompleteRemote.errcheck = HandleErrorCode
    c_RmaOpCompleteRemote(writer, attributeList, time, win, matchingId)

def EvtWriter_ThreadFork(writer, attributeList, time, model, numberOfRequestedThreads):
    c_ThreadFork = conf.lib.OTF2_EvtWriter_ThreadFork
    c_ThreadFork.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, Paradigm, ctypes.c_uint32 ]
    c_ThreadFork.restype = ErrorCode
    c_ThreadFork.errcheck = HandleErrorCode
    c_ThreadFork(writer, attributeList, time, model, numberOfRequestedThreads)

def EvtWriter_ThreadJoin(writer, attributeList, time, model):
    c_ThreadJoin = conf.lib.OTF2_EvtWriter_ThreadJoin
    c_ThreadJoin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, Paradigm ]
    c_ThreadJoin.restype = ErrorCode
    c_ThreadJoin.errcheck = HandleErrorCode
    c_ThreadJoin(writer, attributeList, time, model)

def EvtWriter_ThreadTeamBegin(writer, attributeList, time, threadTeam):
    c_ThreadTeamBegin = conf.lib.OTF2_EvtWriter_ThreadTeamBegin
    c_ThreadTeamBegin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef ]
    c_ThreadTeamBegin.restype = ErrorCode
    c_ThreadTeamBegin.errcheck = HandleErrorCode
    c_ThreadTeamBegin(writer, attributeList, time, threadTeam)

def EvtWriter_ThreadTeamEnd(writer, attributeList, time, threadTeam):
    c_ThreadTeamEnd = conf.lib.OTF2_EvtWriter_ThreadTeamEnd
    c_ThreadTeamEnd.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef ]
    c_ThreadTeamEnd.restype = ErrorCode
    c_ThreadTeamEnd.errcheck = HandleErrorCode
    c_ThreadTeamEnd(writer, attributeList, time, threadTeam)

def EvtWriter_ThreadAcquireLock(writer, attributeList, time, model, lockID, acquisitionOrder):
    c_ThreadAcquireLock = conf.lib.OTF2_EvtWriter_ThreadAcquireLock
    c_ThreadAcquireLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, Paradigm, ctypes.c_uint32, ctypes.c_uint32 ]
    c_ThreadAcquireLock.restype = ErrorCode
    c_ThreadAcquireLock.errcheck = HandleErrorCode
    c_ThreadAcquireLock(writer, attributeList, time, model, lockID, acquisitionOrder)

def EvtWriter_ThreadReleaseLock(writer, attributeList, time, model, lockID, acquisitionOrder):
    c_ThreadReleaseLock = conf.lib.OTF2_EvtWriter_ThreadReleaseLock
    c_ThreadReleaseLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, Paradigm, ctypes.c_uint32, ctypes.c_uint32 ]
    c_ThreadReleaseLock.restype = ErrorCode
    c_ThreadReleaseLock.errcheck = HandleErrorCode
    c_ThreadReleaseLock(writer, attributeList, time, model, lockID, acquisitionOrder)

def EvtWriter_ThreadTaskCreate(writer, attributeList, time, threadTeam, creatingThread, generationNumber):
    c_ThreadTaskCreate = conf.lib.OTF2_EvtWriter_ThreadTaskCreate
    c_ThreadTaskCreate.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef, ctypes.c_uint32, ctypes.c_uint32 ]
    c_ThreadTaskCreate.restype = ErrorCode
    c_ThreadTaskCreate.errcheck = HandleErrorCode
    c_ThreadTaskCreate(writer, attributeList, time, threadTeam, creatingThread, generationNumber)

def EvtWriter_ThreadTaskSwitch(writer, attributeList, time, threadTeam, creatingThread, generationNumber):
    c_ThreadTaskSwitch = conf.lib.OTF2_EvtWriter_ThreadTaskSwitch
    c_ThreadTaskSwitch.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef, ctypes.c_uint32, ctypes.c_uint32 ]
    c_ThreadTaskSwitch.restype = ErrorCode
    c_ThreadTaskSwitch.errcheck = HandleErrorCode
    c_ThreadTaskSwitch(writer, attributeList, time, threadTeam, creatingThread, generationNumber)

def EvtWriter_ThreadTaskComplete(writer, attributeList, time, threadTeam, creatingThread, generationNumber):
    c_ThreadTaskComplete = conf.lib.OTF2_EvtWriter_ThreadTaskComplete
    c_ThreadTaskComplete.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef, ctypes.c_uint32, ctypes.c_uint32 ]
    c_ThreadTaskComplete.restype = ErrorCode
    c_ThreadTaskComplete.errcheck = HandleErrorCode
    c_ThreadTaskComplete(writer, attributeList, time, threadTeam, creatingThread, generationNumber)

def EvtWriter_ThreadCreate(writer, attributeList, time, threadContingent, sequenceCount):
    c_ThreadCreate = conf.lib.OTF2_EvtWriter_ThreadCreate
    c_ThreadCreate.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef, ctypes.c_uint64 ]
    c_ThreadCreate.restype = ErrorCode
    c_ThreadCreate.errcheck = HandleErrorCode
    c_ThreadCreate(writer, attributeList, time, threadContingent, sequenceCount)

def EvtWriter_ThreadBegin(writer, attributeList, time, threadContingent, sequenceCount):
    c_ThreadBegin = conf.lib.OTF2_EvtWriter_ThreadBegin
    c_ThreadBegin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef, ctypes.c_uint64 ]
    c_ThreadBegin.restype = ErrorCode
    c_ThreadBegin.errcheck = HandleErrorCode
    c_ThreadBegin(writer, attributeList, time, threadContingent, sequenceCount)

def EvtWriter_ThreadWait(writer, attributeList, time, threadContingent, sequenceCount):
    c_ThreadWait = conf.lib.OTF2_EvtWriter_ThreadWait
    c_ThreadWait.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef, ctypes.c_uint64 ]
    c_ThreadWait.restype = ErrorCode
    c_ThreadWait.errcheck = HandleErrorCode
    c_ThreadWait(writer, attributeList, time, threadContingent, sequenceCount)

def EvtWriter_ThreadEnd(writer, attributeList, time, threadContingent, sequenceCount):
    c_ThreadEnd = conf.lib.OTF2_EvtWriter_ThreadEnd
    c_ThreadEnd.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CommRef, ctypes.c_uint64 ]
    c_ThreadEnd.restype = ErrorCode
    c_ThreadEnd.errcheck = HandleErrorCode
    c_ThreadEnd(writer, attributeList, time, threadContingent, sequenceCount)

def EvtWriter_CallingContextEnter(writer, attributeList, time, callingContext, unwindDistance):
    c_CallingContextEnter = conf.lib.OTF2_EvtWriter_CallingContextEnter
    c_CallingContextEnter.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CallingContextRef, ctypes.c_uint32 ]
    c_CallingContextEnter.restype = ErrorCode
    c_CallingContextEnter.errcheck = HandleErrorCode
    c_CallingContextEnter(writer, attributeList, time, callingContext, unwindDistance)

def EvtWriter_CallingContextLeave(writer, attributeList, time, callingContext):
    c_CallingContextLeave = conf.lib.OTF2_EvtWriter_CallingContextLeave
    c_CallingContextLeave.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CallingContextRef ]
    c_CallingContextLeave.restype = ErrorCode
    c_CallingContextLeave.errcheck = HandleErrorCode
    c_CallingContextLeave(writer, attributeList, time, callingContext)

def EvtWriter_CallingContextSample(writer, attributeList, time, callingContext, unwindDistance, interruptGenerator):
    c_CallingContextSample = conf.lib.OTF2_EvtWriter_CallingContextSample
    c_CallingContextSample.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, CallingContextRef, ctypes.c_uint32, InterruptGeneratorRef ]
    c_CallingContextSample.restype = ErrorCode
    c_CallingContextSample.errcheck = HandleErrorCode
    c_CallingContextSample(writer, attributeList, time, callingContext, unwindDistance, interruptGenerator)

def EvtWriter_IoCreateHandle(writer, attributeList, time, handle, mode, creationFlags, statusFlags):
    c_IoCreateHandle = conf.lib.OTF2_EvtWriter_IoCreateHandle
    c_IoCreateHandle.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, IoAccessMode, IoCreationFlag, IoStatusFlag ]
    c_IoCreateHandle.restype = ErrorCode
    c_IoCreateHandle.errcheck = HandleErrorCode
    c_IoCreateHandle(writer, attributeList, time, handle, mode, creationFlags, statusFlags)

def EvtWriter_IoDestroyHandle(writer, attributeList, time, handle):
    c_IoDestroyHandle = conf.lib.OTF2_EvtWriter_IoDestroyHandle
    c_IoDestroyHandle.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef ]
    c_IoDestroyHandle.restype = ErrorCode
    c_IoDestroyHandle.errcheck = HandleErrorCode
    c_IoDestroyHandle(writer, attributeList, time, handle)

def EvtWriter_IoDuplicateHandle(writer, attributeList, time, oldHandle, newHandle, statusFlags):
    c_IoDuplicateHandle = conf.lib.OTF2_EvtWriter_IoDuplicateHandle
    c_IoDuplicateHandle.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, IoHandleRef, IoStatusFlag ]
    c_IoDuplicateHandle.restype = ErrorCode
    c_IoDuplicateHandle.errcheck = HandleErrorCode
    c_IoDuplicateHandle(writer, attributeList, time, oldHandle, newHandle, statusFlags)

def EvtWriter_IoSeek(writer, attributeList, time, handle, offsetRequest, whence, offsetResult):
    c_IoSeek = conf.lib.OTF2_EvtWriter_IoSeek
    c_IoSeek.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, ctypes.c_int64, IoSeekOption, ctypes.c_uint64 ]
    c_IoSeek.restype = ErrorCode
    c_IoSeek.errcheck = HandleErrorCode
    c_IoSeek(writer, attributeList, time, handle, offsetRequest, whence, offsetResult)

def EvtWriter_IoChangeStatusFlags(writer, attributeList, time, handle, statusFlags):
    c_IoChangeStatusFlags = conf.lib.OTF2_EvtWriter_IoChangeStatusFlags
    c_IoChangeStatusFlags.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, IoStatusFlag ]
    c_IoChangeStatusFlags.restype = ErrorCode
    c_IoChangeStatusFlags.errcheck = HandleErrorCode
    c_IoChangeStatusFlags(writer, attributeList, time, handle, statusFlags)

def EvtWriter_IoDeleteFile(writer, attributeList, time, ioParadigm, file):
    c_IoDeleteFile = conf.lib.OTF2_EvtWriter_IoDeleteFile
    c_IoDeleteFile.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoParadigmRef, IoFileRef ]
    c_IoDeleteFile.restype = ErrorCode
    c_IoDeleteFile.errcheck = HandleErrorCode
    c_IoDeleteFile(writer, attributeList, time, ioParadigm, file)

def EvtWriter_IoOperationBegin(writer, attributeList, time, handle, mode, operationFlags, bytesRequest, matchingId):
    c_IoOperationBegin = conf.lib.OTF2_EvtWriter_IoOperationBegin
    c_IoOperationBegin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, IoOperationMode, IoOperationFlag, ctypes.c_uint64, ctypes.c_uint64 ]
    c_IoOperationBegin.restype = ErrorCode
    c_IoOperationBegin.errcheck = HandleErrorCode
    c_IoOperationBegin(writer, attributeList, time, handle, mode, operationFlags, bytesRequest, matchingId)

def EvtWriter_IoOperationTest(writer, attributeList, time, handle, matchingId):
    c_IoOperationTest = conf.lib.OTF2_EvtWriter_IoOperationTest
    c_IoOperationTest.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, ctypes.c_uint64 ]
    c_IoOperationTest.restype = ErrorCode
    c_IoOperationTest.errcheck = HandleErrorCode
    c_IoOperationTest(writer, attributeList, time, handle, matchingId)

def EvtWriter_IoOperationIssued(writer, attributeList, time, handle, matchingId):
    c_IoOperationIssued = conf.lib.OTF2_EvtWriter_IoOperationIssued
    c_IoOperationIssued.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, ctypes.c_uint64 ]
    c_IoOperationIssued.restype = ErrorCode
    c_IoOperationIssued.errcheck = HandleErrorCode
    c_IoOperationIssued(writer, attributeList, time, handle, matchingId)

def EvtWriter_IoOperationComplete(writer, attributeList, time, handle, bytesResult, matchingId):
    c_IoOperationComplete = conf.lib.OTF2_EvtWriter_IoOperationComplete
    c_IoOperationComplete.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, ctypes.c_uint64, ctypes.c_uint64 ]
    c_IoOperationComplete.restype = ErrorCode
    c_IoOperationComplete.errcheck = HandleErrorCode
    c_IoOperationComplete(writer, attributeList, time, handle, bytesResult, matchingId)

def EvtWriter_IoOperationCancelled(writer, attributeList, time, handle, matchingId):
    c_IoOperationCancelled = conf.lib.OTF2_EvtWriter_IoOperationCancelled
    c_IoOperationCancelled.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, ctypes.c_uint64 ]
    c_IoOperationCancelled.restype = ErrorCode
    c_IoOperationCancelled.errcheck = HandleErrorCode
    c_IoOperationCancelled(writer, attributeList, time, handle, matchingId)

def EvtWriter_IoAcquireLock(writer, attributeList, time, handle, lockType):
    c_IoAcquireLock = conf.lib.OTF2_EvtWriter_IoAcquireLock
    c_IoAcquireLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, LockType ]
    c_IoAcquireLock.restype = ErrorCode
    c_IoAcquireLock.errcheck = HandleErrorCode
    c_IoAcquireLock(writer, attributeList, time, handle, lockType)

def EvtWriter_IoReleaseLock(writer, attributeList, time, handle, lockType):
    c_IoReleaseLock = conf.lib.OTF2_EvtWriter_IoReleaseLock
    c_IoReleaseLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, LockType ]
    c_IoReleaseLock.restype = ErrorCode
    c_IoReleaseLock.errcheck = HandleErrorCode
    c_IoReleaseLock(writer, attributeList, time, handle, lockType)

def EvtWriter_IoTryLock(writer, attributeList, time, handle, lockType):
    c_IoTryLock = conf.lib.OTF2_EvtWriter_IoTryLock
    c_IoTryLock.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, IoHandleRef, LockType ]
    c_IoTryLock.restype = ErrorCode
    c_IoTryLock.errcheck = HandleErrorCode
    c_IoTryLock(writer, attributeList, time, handle, lockType)

def EvtWriter_ProgramBegin(writer, attributeList, time, programName, programArguments):
    numberOfArguments = len(programArguments)
    StringRefArrayType = StringRef * numberOfArguments
    argument_list = StringRefArrayType()
    argument_list[:] = programArguments

    c_ProgramBegin = conf.lib.OTF2_EvtWriter_ProgramBegin
    c_ProgramBegin.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, StringRef, ctypes.c_uint32, StringRefArrayType ]
    c_ProgramBegin.restype = ErrorCode
    c_ProgramBegin.errcheck = HandleErrorCode
    c_ProgramBegin(writer, attributeList, time , programName, numberOfArguments, argument_list)

def EvtWriter_ProgramEnd(writer, attributeList, time, exitStatus):
    c_ProgramEnd = conf.lib.OTF2_EvtWriter_ProgramEnd
    c_ProgramEnd.argtypes = [ ctypes.POINTER(EvtWriter), ctypes.POINTER(AttributeList), TimeStamp, ctypes.c_int64 ]
    c_ProgramEnd.restype = ErrorCode
    c_ProgramEnd.errcheck = HandleErrorCode
    c_ProgramEnd(writer, attributeList, time, exitStatus)

__all__ = [
    'EvtWriter',
    'EvtWriter_GetLocationID',
    'EvtWriter_SetUserData',
    'EvtWriter_GetUserData',
    'EvtWriter_SetLocationID',
    'EvtWriter_GetNumberOfEvents',
    'EvtWriter_StoreRewindPoint',
    'EvtWriter_Rewind',
    'EvtWriter_ClearRewindPoint',
    'EvtWriter_BufferFlush',
    'EvtWriter_MeasurementOnOff',
    'EvtWriter_Enter',
    'EvtWriter_Leave',
    'EvtWriter_MpiSend',
    'EvtWriter_MpiIsend',
    'EvtWriter_MpiIsendComplete',
    'EvtWriter_MpiIrecvRequest',
    'EvtWriter_MpiRecv',
    'EvtWriter_MpiIrecv',
    'EvtWriter_MpiRequestTest',
    'EvtWriter_MpiRequestCancelled',
    'EvtWriter_MpiCollectiveBegin',
    'EvtWriter_MpiCollectiveEnd',
    'EvtWriter_OmpFork',
    'EvtWriter_OmpJoin',
    'EvtWriter_OmpAcquireLock',
    'EvtWriter_OmpReleaseLock',
    'EvtWriter_OmpTaskCreate',
    'EvtWriter_OmpTaskSwitch',
    'EvtWriter_OmpTaskComplete',
    'EvtWriter_Metric',
    'EvtWriter_ParameterString',
    'EvtWriter_ParameterInt',
    'EvtWriter_ParameterUnsignedInt',
    'EvtWriter_RmaWinCreate',
    'EvtWriter_RmaWinDestroy',
    'EvtWriter_RmaCollectiveBegin',
    'EvtWriter_RmaCollectiveEnd',
    'EvtWriter_RmaGroupSync',
    'EvtWriter_RmaRequestLock',
    'EvtWriter_RmaAcquireLock',
    'EvtWriter_RmaTryLock',
    'EvtWriter_RmaReleaseLock',
    'EvtWriter_RmaSync',
    'EvtWriter_RmaWaitChange',
    'EvtWriter_RmaPut',
    'EvtWriter_RmaGet',
    'EvtWriter_RmaAtomic',
    'EvtWriter_RmaOpCompleteBlocking',
    'EvtWriter_RmaOpCompleteNonBlocking',
    'EvtWriter_RmaOpTest',
    'EvtWriter_RmaOpCompleteRemote',
    'EvtWriter_ThreadFork',
    'EvtWriter_ThreadJoin',
    'EvtWriter_ThreadTeamBegin',
    'EvtWriter_ThreadTeamEnd',
    'EvtWriter_ThreadAcquireLock',
    'EvtWriter_ThreadReleaseLock',
    'EvtWriter_ThreadTaskCreate',
    'EvtWriter_ThreadTaskSwitch',
    'EvtWriter_ThreadTaskComplete',
    'EvtWriter_ThreadCreate',
    'EvtWriter_ThreadBegin',
    'EvtWriter_ThreadWait',
    'EvtWriter_ThreadEnd',
    'EvtWriter_CallingContextEnter',
    'EvtWriter_CallingContextLeave',
    'EvtWriter_CallingContextSample',
    'EvtWriter_IoCreateHandle',
    'EvtWriter_IoDestroyHandle',
    'EvtWriter_IoDuplicateHandle',
    'EvtWriter_IoSeek',
    'EvtWriter_IoChangeStatusFlags',
    'EvtWriter_IoDeleteFile',
    'EvtWriter_IoOperationBegin',
    'EvtWriter_IoOperationTest',
    'EvtWriter_IoOperationIssued',
    'EvtWriter_IoOperationComplete',
    'EvtWriter_IoOperationCancelled',
    'EvtWriter_IoAcquireLock',
    'EvtWriter_IoReleaseLock',
    'EvtWriter_IoTryLock',
    'EvtWriter_ProgramBegin',
    'EvtWriter_ProgramEnd',
]
