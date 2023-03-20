# ConversationsMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Message ID. It can be used for further manipulations with the message. | [optional] 
**type** | **str** | &#x60;\&quot;agent\&quot;&#x60; for agents’ messages, &#x60;\&quot;visitor\&quot;&#x60; for visitors’ messages. | [optional] 
**text** | **str** | Message text or name of the attached file | [optional] 
**visitor_id** | **str** | visitor’s ID | [optional] 
**agent_id** | **str** | ID of the agent on whose behalf the message was sent (only in messages sent by an agent). | [optional] 
**agent_name** | **str** | Agent’s name as displayed to the visitor. Only in the messages sent by an agent. | [optional] 
**created_at** | **int** | Timestamp in milliseconds. | [optional] 
**is_pushed** | **bool** | &#x60;true&#x60; for pushed messages | [optional] 
**received_from** | **str** | In two-way integrations, messages sent via REST API can be marked with receivedFrom property and then filtered out when received in a webhook to avoid infinite loop. | [optional] 
**file** | [**ConversationsMessageFile**](ConversationsMessageFile.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


