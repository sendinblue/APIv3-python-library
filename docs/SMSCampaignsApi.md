# sib_api_v3_sdk.SMSCampaignsApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sms_campaign**](SMSCampaignsApi.md#create_sms_campaign) | **POST** /smsCampaigns | Creates an SMS campaign
[**delete_sms_campaign**](SMSCampaignsApi.md#delete_sms_campaign) | **DELETE** /smsCampaigns/{campaignId} | Delete the SMS campaign
[**get_sms_campaign**](SMSCampaignsApi.md#get_sms_campaign) | **GET** /smsCampaigns/{campaignId} | Get an SMS campaign
[**get_sms_campaigns**](SMSCampaignsApi.md#get_sms_campaigns) | **GET** /smsCampaigns | Returns the informations for all your created SMS campaigns
[**request_sms_recipient_export**](SMSCampaignsApi.md#request_sms_recipient_export) | **POST** /smsCampaigns/{campaignId}/exportRecipients | Exports the recipients of the specified campaign.
[**send_sms_campaign_now**](SMSCampaignsApi.md#send_sms_campaign_now) | **POST** /smsCampaigns/{campaignId}/sendNow | Send your SMS campaign immediately
[**send_sms_report**](SMSCampaignsApi.md#send_sms_report) | **POST** /smsCampaigns/{campaignId}/sendReport | Send report of SMS campaigns
[**send_test_sms**](SMSCampaignsApi.md#send_test_sms) | **POST** /smsCampaigns/{campaignId}/sendTest | Send an SMS
[**update_sms_campaign**](SMSCampaignsApi.md#update_sms_campaign) | **PUT** /smsCampaigns/{campaignId} | Updates an SMS campaign
[**update_sms_campaign_status**](SMSCampaignsApi.md#update_sms_campaign_status) | **PUT** /smsCampaigns/{campaignId}/status | Update the campaign status

# **create_sms_campaign**
> CreateModel create_sms_campaign(body)

Creates an SMS campaign

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.CreateSmsCampaign() # CreateSmsCampaign | Values to create an SMS Campaign

try:
    # Creates an SMS campaign
    api_response = api_instance.create_sms_campaign(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->create_sms_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSmsCampaign**](CreateSmsCampaign.md)| Values to create an SMS Campaign | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sms_campaign**
> delete_sms_campaign(campaign_id)

Delete the SMS campaign

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 56 # int | id of the SMS campaign

try:
    # Delete the SMS campaign
    api_instance.delete_sms_campaign(campaign_id)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->delete_sms_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**int**](.md)| id of the SMS campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sms_campaign**
> GetSmsCampaign get_sms_campaign(campaign_id)

Get an SMS campaign

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 56 # int | id of the SMS campaign

try:
    # Get an SMS campaign
    api_response = api_instance.get_sms_campaign(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->get_sms_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**int**](.md)| id of the SMS campaign | 

### Return type

[**GetSmsCampaign**](GetSmsCampaign.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sms_campaigns**
> GetSmsCampaigns get_sms_campaigns(status=status, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

Returns the informations for all your created SMS campaigns

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
status = 'status_example' # str | Status of campaign. (optional)
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent sms campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either 'status' not passed and if passed is set to 'sent' ) (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent sms campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either 'status' not passed and if passed is set to 'sent' ) (optional)
limit = 56 # int | Number limitation for the result returned (optional)
offset = 56 # int | Beginning point in the list to retrieve from. (optional)

try:
    # Returns the informations for all your created SMS campaigns
    api_response = api_instance.get_sms_campaigns(status=status, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->get_sms_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**str**](.md)| Status of campaign. | [optional] 
 **start_date** | [**str**](.md)| Mandatory if endDate is used. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent sms campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either &#x27;status&#x27; not passed and if passed is set to &#x27;sent&#x27; ) | [optional] 
 **end_date** | [**str**](.md)| Mandatory if startDate is used. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the sent sms campaigns. Prefer to pass your timezone in date-time format for accurate result ( only available if either &#x27;status&#x27; not passed and if passed is set to &#x27;sent&#x27; ) | [optional] 
 **limit** | [**int**](.md)| Number limitation for the result returned | [optional] 
 **offset** | [**int**](.md)| Beginning point in the list to retrieve from. | [optional] 

### Return type

[**GetSmsCampaigns**](GetSmsCampaigns.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_sms_recipient_export**
> CreatedProcessId request_sms_recipient_export(campaign_id, body=body)

Exports the recipients of the specified campaign.

It returns the background process ID which on completion calls the notify URL that you have set in the input.

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 56 # int | id of the campaign
body = sib_api_v3_sdk.RequestSmsRecipientExport() # RequestSmsRecipientExport | Values to send for a recipient export request (optional)

try:
    # Exports the recipients of the specified campaign.
    api_response = api_instance.request_sms_recipient_export(campaign_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->request_sms_recipient_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**int**](.md)| id of the campaign | 
 **body** | [**RequestSmsRecipientExport**](RequestSmsRecipientExport.md)| Values to send for a recipient export request | [optional] 

### Return type

[**CreatedProcessId**](CreatedProcessId.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_campaign_now**
> send_sms_campaign_now(campaign_id)

Send your SMS campaign immediately

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 56 # int | id of the campaign

try:
    # Send your SMS campaign immediately
    api_instance.send_sms_campaign_now(campaign_id)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->send_sms_campaign_now: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**int**](.md)| id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_report**
> send_sms_report(body, campaign_id)

Send report of SMS campaigns

Send report of Sent and Archived campaign, to the specified email addresses, with respective data and a pdf attachment in detail.

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.SendReport() # SendReport | Values for send a report
campaign_id = 56 # int | id of the campaign

try:
    # Send report of SMS campaigns
    api_instance.send_sms_report(body, campaign_id)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->send_sms_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendReport**](SendReport.md)| Values for send a report | 
 **campaign_id** | [**int**](.md)| id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_sms**
> send_test_sms(body, campaign_id)

Send an SMS

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.SendTestSms() # SendTestSms | Mobile number of the recipient with the country code. This number must belong to one of your contacts in SendinBlue account and must not be blacklisted
campaign_id = 56 # int | Id of the SMS campaign

try:
    # Send an SMS
    api_instance.send_test_sms(body, campaign_id)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->send_test_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendTestSms**](SendTestSms.md)| Mobile number of the recipient with the country code. This number must belong to one of your contacts in SendinBlue account and must not be blacklisted | 
 **campaign_id** | [**int**](.md)| Id of the SMS campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sms_campaign**
> update_sms_campaign(body, campaign_id)

Updates an SMS campaign

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.UpdateSmsCampaign() # UpdateSmsCampaign | Values to update an SMS Campaign
campaign_id = 56 # int | id of the SMS campaign

try:
    # Updates an SMS campaign
    api_instance.update_sms_campaign(body, campaign_id)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->update_sms_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSmsCampaign**](UpdateSmsCampaign.md)| Values to update an SMS Campaign | 
 **campaign_id** | [**int**](.md)| id of the SMS campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sms_campaign_status**
> update_sms_campaign_status(body, campaign_id)

Update the campaign status

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
api_instance = sib_api_v3_sdk.SMSCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.UpdateCampaignStatus() # UpdateCampaignStatus | Status of the campaign.
campaign_id = 56 # int | id of the campaign

try:
    # Update the campaign status
    api_instance.update_sms_campaign_status(body, campaign_id)
except ApiException as e:
    print("Exception when calling SMSCampaignsApi->update_sms_campaign_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCampaignStatus**](UpdateCampaignStatus.md)| Status of the campaign. | 
 **campaign_id** | [**int**](.md)| id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

