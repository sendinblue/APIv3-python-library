# RequestContactExport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_attributes** | **list[str]** | List of all the attributes that you want to export. These attributes must be present in your contact database. For example, [&#39;fname&#39;, &#39;lname&#39;, &#39;email&#39;]. | [optional] 
**contact_filter** | **object** | This attribute has been deprecated and will be removed by January 1st, 2021. Only one of the two filter options (contactFilter or customContactFilter) can be passed in the request. Set the filter for the contacts to be exported. For example, {\&quot;blacklisted\&quot;:true} will export all the blacklisted contacts.  | [optional] 
**custom_contact_filter** | [**RequestContactExportCustomContactFilter**](RequestContactExportCustomContactFilter.md) |  | [optional] 
**notify_url** | **str** | Webhook that will be called once the export process is finished | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


