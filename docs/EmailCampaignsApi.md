# sib_api_v3_sdk.EmailCampaignsApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_campaign**](EmailCampaignsApi.md#create_email_campaign) | **POST** /emailCampaigns | Create an email campaign
[**delete_email_campaigns**](EmailCampaignsApi.md#delete_email_campaigns) | **DELETE** /emailCampaigns/{campaignId} | Delete an email campaign
[**email_export_recipients**](EmailCampaignsApi.md#email_export_recipients) | **POST** /emailCampaigns/{campaignId}/exportRecipients | Export the recipients of a campaign
[**get_email_campaign**](EmailCampaignsApi.md#get_email_campaign) | **GET** /emailCampaigns/{campaignId} | Get campaign informations
[**get_email_campaigns**](EmailCampaignsApi.md#get_email_campaigns) | **GET** /emailCampaigns | Return all your created campaigns
[**send_email_campaign_now**](EmailCampaignsApi.md#send_email_campaign_now) | **POST** /emailCampaigns/{campaignId}/sendNow | Send an email campaign id of the campaign immediately
[**send_report**](EmailCampaignsApi.md#send_report) | **POST** /emailCampaigns/{campaignId}/sendReport | Send the report of a campaigns
[**send_test_email**](EmailCampaignsApi.md#send_test_email) | **POST** /emailCampaigns/{campaignId}/sendTest | Send an email campaign to your test list
[**update_campaign_status**](EmailCampaignsApi.md#update_campaign_status) | **PUT** /emailCampaigns/{campaignId}/status | Update a campaign status
[**update_email_campaigns**](EmailCampaignsApi.md#update_email_campaigns) | **PUT** /emailCampaigns/{campaignId} | Update a campaign


# **create_email_campaign**
> CreateModel create_email_campaign(email_campaigns)

Create an email campaign

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign() # CreateEmailCampaign | Values to create a campaign

try: 
    # Create an email campaign
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaigns** | [**CreateEmailCampaign**](CreateEmailCampaign.md)| Values to create a campaign | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_campaigns**
> delete_email_campaigns(campaign_id)

Delete an email campaign

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | id of the campaign

try: 
    # Delete an email campaign
    api_instance.delete_email_campaigns(campaign_id)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->delete_email_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_export_recipients**
> CreatedProcessId email_export_recipients(campaign_id, recipient_export=recipient_export)

Export the recipients of a campaign

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | Id of the campaign
recipient_export = sib_api_v3_sdk.EmailExportRecipients() # EmailExportRecipients | Values to send for a recipient export request (optional)

try: 
    # Export the recipients of a campaign
    api_response = api_instance.email_export_recipients(campaign_id, recipient_export=recipient_export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->email_export_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 
 **recipient_export** | [**EmailExportRecipients**](EmailExportRecipients.md)| Values to send for a recipient export request | [optional] 

### Return type

[**CreatedProcessId**](CreatedProcessId.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign**
> GetEmailCampaign get_email_campaign(campaign_id)

Get campaign informations

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | Id of the campaign

try: 
    # Get campaign informations
    api_response = api_instance.get_email_campaign(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->get_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 

### Return type

[**GetEmailCampaign**](GetEmailCampaign.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns**
> GetEmailCampaigns get_email_campaigns(type=type, status=status, limit=limit, offset=offset)

Return all your created campaigns

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
type = 'type_example' # str | Filter on the type of the campaigns (optional)
status = 'status_example' # str | Filter on the status of the campaign (optional)
limit = 500 # int | Number of documents per page (optional) (default to 500)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)

try: 
    # Return all your created campaigns
    api_response = api_instance.get_email_campaigns(type=type, status=status, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->get_email_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter on the type of the campaigns | [optional] 
 **status** | **str**| Filter on the status of the campaign | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 500]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]

### Return type

[**GetEmailCampaigns**](GetEmailCampaigns.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_campaign_now**
> send_email_campaign_now(campaign_id)

Send an email campaign id of the campaign immediately

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | Id of the campaign

try: 
    # Send an email campaign id of the campaign immediately
    api_instance.send_email_campaign_now(campaign_id)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->send_email_campaign_now: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_report**
> send_report(campaign_id, send_report)

Send the report of a campaigns

A PDF will be sent to the specified email addresses

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | Id of the campaign
send_report = sib_api_v3_sdk.SendReport() # SendReport | Values for send a report

try: 
    # Send the report of a campaigns
    api_instance.send_report(campaign_id, send_report)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->send_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 
 **send_report** | [**SendReport**](SendReport.md)| Values for send a report | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_email**
> send_test_email(campaign_id, email_to)

Send an email campaign to your test list

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | Id of the campaign
email_to = sib_api_v3_sdk.SendTestEmail() # SendTestEmail | 

try: 
    # Send an email campaign to your test list
    api_instance.send_test_email(campaign_id, email_to)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->send_test_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 
 **email_to** | [**SendTestEmail**](SendTestEmail.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_status**
> update_campaign_status(campaign_id, status)

Update a campaign status

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | Id of the campaign
status = sib_api_v3_sdk.UpdateCampaignStatus() # UpdateCampaignStatus | Status of the campaign

try: 
    # Update a campaign status
    api_instance.update_campaign_status(campaign_id, status)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->update_campaign_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 
 **status** | [**UpdateCampaignStatus**](UpdateCampaignStatus.md)| Status of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_campaigns**
> update_email_campaigns(campaign_id, email_campaign)

Update a campaign

### Example 
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
campaign_id = 789 # int | Id of the campaign
email_campaign = sib_api_v3_sdk.UpdateEmailCampaign() # UpdateEmailCampaign | Values to update a campaign

try: 
    # Update a campaign
    api_instance.update_email_campaigns(campaign_id, email_campaign)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->update_email_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 
 **email_campaign** | [**UpdateEmailCampaign**](UpdateEmailCampaign.md)| Values to update a campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

