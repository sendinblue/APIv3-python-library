# RequestContactExport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_attributes** | **list[str]** | List of all the attributes that you want to export. These attributes must be present in your contact database. For example, [&#x27;fname&#x27;, &#x27;lname&#x27;, &#x27;email&#x27;]. | [optional] 
**contact_filter** | **object** | Set the filter for the contacts to be exported. For example, &#x60;{\&quot;blacklisted\&quot;:true}&#x60; will export all the blacklisted contacts. | 
**notify_url** | **str** | Webhook that will be called once the export process is finished | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

