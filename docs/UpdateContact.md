# UpdateContact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** | Pass the set of attributes to be updated. These attributes must be present in your account. To update existing email address of a contact with the new one please pass EMAIL in attribtes. For eg. { &#39;EMAIL&#39;:&#39;newemail@domain.com&#39;, &#39;FNAME&#39;:&#39;Ellie&#39;, &#39;LNAME&#39;:&#39;Roger&#39;} | [optional] 
**email_blacklisted** | **bool** | Set/unset this field to blacklist/allow the contact for emails (emailBlacklisted &#x3D; true) | [optional] 
**sms_blacklisted** | **bool** | Set/unset this field to blacklist/allow the contact for SMS (smsBlacklisted &#x3D; true) | [optional] 
**list_ids** | **list[int]** | Ids of the lists to add the contact to | [optional] 
**unlink_list_ids** | **list[int]** | Ids of the lists to remove the contact from | [optional] 
**smtp_blacklist_sender** | **list[str]** | transactional email forbidden sender for contact. Use only for email Contact | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


