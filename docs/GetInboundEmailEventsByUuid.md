# GetInboundEmailEventsByUuid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**received_at** | **datetime** | Date when email was received on SMTP relay | [optional] 
**delivered_at** | **datetime** | Date when email was delivered successfully to client’s webhook | [optional] 
**recipient** | **str** | Recipient’s email address | [optional] 
**sender** | **str** | Sender’s email address | [optional] 
**message_id** | **str** | Value of the Message-ID header. This will be present only after the processing is done. | [optional] 
**subject** | **str** | Value of the Subject header. This will be present only after the processing is done.  | [optional] 
**attachments** | [**list[GetInboundEmailEventsByUuidAttachments]**](GetInboundEmailEventsByUuidAttachments.md) | List of attachments of the email. This will be present only after the processing is done. | [optional] 
**logs** | [**list[GetInboundEmailEventsByUuidLogs]**](GetInboundEmailEventsByUuidLogs.md) | List of events/logs that describe the lifecycle of the email on SIB platform | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


