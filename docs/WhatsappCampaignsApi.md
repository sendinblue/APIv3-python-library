# sib_api_v3_sdk.WhatsappCampaignsApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_whatsapp_campaign**](WhatsappCampaignsApi.md#delete_whatsapp_campaign) | **DELETE** /whatsappCampaigns/{campaignId} | Delete a Whatsapp campaign
[**get_whatsapp_campaign**](WhatsappCampaignsApi.md#get_whatsapp_campaign) | **GET** /whatsappCampaigns/{campaignId} | Get a Whatsapp campaign
[**get_whatsapp_templates**](WhatsappCampaignsApi.md#get_whatsapp_templates) | **GET** /whatsappCampaigns/template-list | Return all your created whatsapp templates


# **delete_whatsapp_campaign**
> delete_whatsapp_campaign(campaign_id)

Delete a Whatsapp campaign

### Example
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.WhatsappCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | id of the campaign

try:
    # Delete a Whatsapp campaign
    api_instance.delete_whatsapp_campaign(campaign_id)
except ApiException as e:
    print("Exception when calling WhatsappCampaignsApi->delete_whatsapp_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whatsapp_campaign**
> GetWhatsappCampaignOverview get_whatsapp_campaign(campaign_id)

Get a Whatsapp campaign

### Example
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.WhatsappCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 'campaign_id_example' # str | Id of the campaign

try:
    # Get a Whatsapp campaign
    api_response = api_instance.get_whatsapp_campaign(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsappCampaignsApi->get_whatsapp_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Id of the campaign | 

### Return type

[**GetWhatsappCampaignOverview**](GetWhatsappCampaignOverview.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whatsapp_templates**
> GetWATemplates get_whatsapp_templates(start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)

Return all your created whatsapp templates

### Example
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.WhatsappCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
start_date = 'start_date_example' # str | **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' )  (optional)
end_date = 'end_date_example' # str | **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' )  (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Return all your created whatsapp templates
    api_response = api_instance.get_whatsapp_templates(start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsappCampaignsApi->get_whatsapp_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either &#39;status&#39; not passed and if passed is set to &#39;sent&#39; )  | [optional] 
 **end_date** | **str**| **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either &#39;status&#39; not passed and if passed is set to &#39;sent&#39; )  | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetWATemplates**](GetWATemplates.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

