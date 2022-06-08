# sib_api_v3_sdk.EmailCampaignsApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_campaign**](EmailCampaignsApi.md#create_email_campaign) | **POST** /emailCampaigns | Create an email campaign
[**delete_email_campaign**](EmailCampaignsApi.md#delete_email_campaign) | **DELETE** /emailCampaigns/{campaignId} | Delete an email campaign
[**email_export_recipients**](EmailCampaignsApi.md#email_export_recipients) | **POST** /emailCampaigns/{campaignId}/exportRecipients | Export the recipients of an email campaign
[**get_ab_test_campaign_result**](EmailCampaignsApi.md#get_ab_test_campaign_result) | **GET** /emailCampaigns/{campaignId}/abTestCampaignResult | Get an A/B test email campaign results
[**get_email_campaign**](EmailCampaignsApi.md#get_email_campaign) | **GET** /emailCampaigns/{campaignId} | Get an email campaign report
[**get_email_campaigns**](EmailCampaignsApi.md#get_email_campaigns) | **GET** /emailCampaigns | Return all your created email campaigns
[**get_shared_template_url**](EmailCampaignsApi.md#get_shared_template_url) | **GET** /emailCampaigns/{campaignId}/sharedUrl | Get a shared template url
[**send_email_campaign_now**](EmailCampaignsApi.md#send_email_campaign_now) | **POST** /emailCampaigns/{campaignId}/sendNow | Send an email campaign immediately, based on campaignId
[**send_report**](EmailCampaignsApi.md#send_report) | **POST** /emailCampaigns/{campaignId}/sendReport | Send the report of a campaign
[**send_test_email**](EmailCampaignsApi.md#send_test_email) | **POST** /emailCampaigns/{campaignId}/sendTest | Send an email campaign to your test list
[**update_campaign_status**](EmailCampaignsApi.md#update_campaign_status) | **PUT** /emailCampaigns/{campaignId}/status | Update an email campaign status
[**update_email_campaign**](EmailCampaignsApi.md#update_email_campaign) | **PUT** /emailCampaigns/{campaignId} | Update an email campaign
[**upload_image_to_gallery**](EmailCampaignsApi.md#upload_image_to_gallery) | **POST** /emailCampaigns/images | Upload an image to your account&#39;s image gallery


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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
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

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_campaign**
> delete_email_campaign(campaign_id)

Delete an email campaign

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | id of the campaign

try:
    # Delete an email campaign
    api_instance.delete_email_campaign(campaign_id)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->delete_email_campaign: %s\n" % e)
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

# **email_export_recipients**
> CreatedProcessId email_export_recipients(campaign_id, recipient_export=recipient_export)

Export the recipients of an email campaign

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign
recipient_export = sib_api_v3_sdk.EmailExportRecipients() # EmailExportRecipients | Values to send for a recipient export request (optional)

try:
    # Export the recipients of an email campaign
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

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ab_test_campaign_result**
> AbTestCampaignResult get_ab_test_campaign_result(campaign_id)

Get an A/B test email campaign results

Obtain winning version of an A/B test email campaign

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the A/B test campaign

try:
    # Get an A/B test email campaign results
    api_response = api_instance.get_ab_test_campaign_result(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->get_ab_test_campaign_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the A/B test campaign | 

### Return type

[**AbTestCampaignResult**](AbTestCampaignResult.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign**
> GetEmailCampaign get_email_campaign(campaign_id)

Get an email campaign report

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign

try:
    # Get an email campaign report
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

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns**
> GetEmailCampaigns get_email_campaigns(type=type, status=status, start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)

Return all your created email campaigns

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
type = 'type_example' # str | Filter on the type of the campaigns (optional)
status = 'status_example' # str | Filter on the status of the campaign (optional)
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent email campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either 'status' not passed and if passed is set to 'sent' ) (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent email campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either 'status' not passed and if passed is set to 'sent' ) (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Return all your created email campaigns
    api_response = api_instance.get_email_campaigns(type=type, status=status, start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->get_email_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter on the type of the campaigns | [optional] 
 **status** | **str**| Filter on the status of the campaign | [optional] 
 **start_date** | **str**| Mandatory if endDate is used. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent email campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either &#39;status&#39; not passed and if passed is set to &#39;sent&#39; ) | [optional] 
 **end_date** | **str**| Mandatory if startDate is used. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent email campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either &#39;status&#39; not passed and if passed is set to &#39;sent&#39; ) | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetEmailCampaigns**](GetEmailCampaigns.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_template_url**
> GetSharedTemplateUrl get_shared_template_url(campaign_id)

Get a shared template url

Get a unique URL to share & import an email template from one Sendinblue account to another.

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign or template

try:
    # Get a shared template url
    api_response = api_instance.get_shared_template_url(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->get_shared_template_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign or template | 

### Return type

[**GetSharedTemplateUrl**](GetSharedTemplateUrl.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_campaign_now**
> send_email_campaign_now(campaign_id)

Send an email campaign immediately, based on campaignId

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign

try:
    # Send an email campaign immediately, based on campaignId
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

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_report**
> send_report(campaign_id, send_report)

Send the report of a campaign

A PDF will be sent to the specified email addresses

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign
send_report = sib_api_v3_sdk.SendReport() # SendReport | Values for send a report

try:
    # Send the report of a campaign
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

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
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

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_status**
> update_campaign_status(campaign_id, status)

Update an email campaign status

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign
status = sib_api_v3_sdk.UpdateCampaignStatus() # UpdateCampaignStatus | Status of the campaign

try:
    # Update an email campaign status
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

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_campaign**
> update_email_campaign(campaign_id, email_campaign)

Update an email campaign

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign
email_campaign = sib_api_v3_sdk.UpdateEmailCampaign() # UpdateEmailCampaign | Values to update a campaign

try:
    # Update an email campaign
    api_instance.update_email_campaign(campaign_id, email_campaign)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->update_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 
 **email_campaign** | [**UpdateEmailCampaign**](UpdateEmailCampaign.md)| Values to update a campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image_to_gallery**
> upload_image_to_gallery(upload_image)

Upload an image to your account's image gallery

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
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
upload_image = sib_api_v3_sdk.UploadImageToGallery() # UploadImageToGallery | Parameters to upload an image

try:
    # Upload an image to your account's image gallery
    api_instance.upload_image_to_gallery(upload_image)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->upload_image_to_gallery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_image** | [**UploadImageToGallery**](UploadImageToGallery.md)| Parameters to upload an image | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

