# GetWhatsappEventReportEvents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_number** | **str** | WhatsApp Number with country code. Example, 85264318721 | 
**_date** | **str** | UTC date-time on which the event has been generated | 
**message_id** | **str** | Message ID which generated the event | 
**event** | **str** | Event which occurred | 
**reason** | **str** | Reason for the event (will be there in case of &#x60;error&#x60; and &#x60;soft-bounce&#x60; events) | [optional] 
**body** | **str** | Text of the reply (will be there only in case of &#x60;reply&#x60; event with text) | [optional] 
**media_url** | **str** | Url of the media reply (will be there only in case of &#x60;reply&#x60; event with media) | [optional] 
**sender_number** | **str** | WhatsApp Number with country code. Example, 85264318721 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


