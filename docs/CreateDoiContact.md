# CreateDoiContact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address where the confirmation email will be sent. This email address will be the identifier for all other contact attributes. | 
**attributes** | **object** | Pass the set of attributes and their values. These attributes must be present in your SendinBlue account. For eg. {&#39;FNAME&#39;:&#39;Elly&#39;, &#39;LNAME&#39;:&#39;Roger&#39;} | [optional] 
**include_list_ids** | **list[int]** | Lists under user account where contact should be added | 
**exclude_list_ids** | **list[int]** | Lists under user account where contact should not be added | [optional] 
**template_id** | **int** | Id of the Double opt-in (DOI) template | 
**redirection_url** | **str** | URL of the web page that user will be redirected to after clicking on the double opt in URL. When editing your DOI template you can reference this URL by using the tag {{ params.DOIurl }}. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


