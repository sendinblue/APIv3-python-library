# GetEmailEventReportEvents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address which generates the event | 
**_date** | **str** | UTC date-time on which the event has been generated | 
**subject** | **str** | Subject of the event | [optional] 
**message_id** | **str** | Message ID which generated the event | 
**event** | **str** | Event which occurred | 
**reason** | **str** | Reason of bounce (only available if the event is hardbounce or softbounce) | [optional] 
**tag** | **str** | Tag of the email which generated the event | [optional] 
**ip** | **str** | IP from which the user has opened the email or clicked on the link (only available if the event is opened or clicks) | [optional] 
**link** | **str** | The link which is sent to the user (only available if the event is requests or opened or clicks) | [optional] 
**_from** | **str** | Sender email from which the emails are sent | [optional] 
**template_id** | **int** | ID of the template (only available if the email is template based) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


