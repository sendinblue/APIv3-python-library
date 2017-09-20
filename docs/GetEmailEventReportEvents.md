# GetEmailEventReportEvents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address which generates the event | 
**date** | **date** | Date on which the event has been generated | 
**subject** | **str** | Subject of the event | [optional] 
**message_id** | **str** | Message ID which generated the event | 
**event** | **str** | Event which occured | 
**reason** | **str** | Reason of bounce (only availble if the event is hardbounce or softbounce) | 
**tag** | **str** | Tag of the email which generated the event | 
**ip** | **str** | IP from which the user has opened the email or clicked on the link (only availble if the event is opened or clicks) | [optional] 
**link** | **str** | The link which is sent to the user (only availble if the event is requests or opened or clicks) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


