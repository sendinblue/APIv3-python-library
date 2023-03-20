# SendTransacSms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Name of the sender. **The number of characters is limited to 11 for alphanumeric characters and 15 for numeric characters** | 
**recipient** | **str** | Mobile number to send SMS with the country code | 
**content** | **str** | Content of the message. If more than 160 characters long, will be sent as multiple text messages | 
**type** | **str** | Type of the SMS. Marketing SMS messages are those sent typically with marketing content. Transactional SMS messages are sent to individuals and are triggered in response to some action, such as a sign-up, purchase, etc. | [optional] [default to 'transactional']
**tag** | **str** | Tag of the message | [optional] 
**web_url** | **str** | Webhook to call for each event triggered by the message (delivered etc.) | [optional] 
**unicode_enabled** | **bool** | Format of the message. It indicates whether the content should be treated as unicode or not. | [optional] [default to False]
**organisation_prefix** | **str** | A recognizable prefix will ensure your audience knows who you are. Recommended by U.S. carriers. This will be added as your Brand Name before the message content. **Prefer verifying maximum length of 160 characters including this prefix in message content to avoid multiple sending of same sms.** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


