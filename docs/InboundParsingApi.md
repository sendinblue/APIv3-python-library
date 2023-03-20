# sib_api_v3_sdk.InboundParsingApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inbound_email_attachment**](InboundParsingApi.md#get_inbound_email_attachment) | **GET** /inbound/attachments/{downloadToken} | Retrieve inbound attachment with download token.
[**get_inbound_email_events**](InboundParsingApi.md#get_inbound_email_events) | **GET** /inbound/events | Get the list of all the events for the received emails.
[**get_inbound_email_events_by_uuid**](InboundParsingApi.md#get_inbound_email_events_by_uuid) | **GET** /inbound/events/{uuid} | Fetch all events history for one particular received email.


# **get_inbound_email_attachment**
> file get_inbound_email_attachment(download_token)

Retrieve inbound attachment with download token.

This endpoint will retrieve inbound attachment with download token.

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
api_instance = sib_api_v3_sdk.InboundParsingApi(sib_api_v3_sdk.ApiClient(configuration))
download_token = 'download_token_example' # str | Token to fetch a particular attachment

try:
    # Retrieve inbound attachment with download token.
    api_response = api_instance.get_inbound_email_attachment(download_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundParsingApi->get_inbound_email_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_token** | **str**| Token to fetch a particular attachment | 

### Return type

[**file**](file.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_email_events**
> GetInboundEmailEvents get_inbound_email_events(sender=sender, start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)

Get the list of all the events for the received emails.

This endpoint will show the list of all the events for the received emails.

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
api_instance = sib_api_v3_sdk.InboundParsingApi(sib_api_v3_sdk.ApiClient(configuration))
sender = 'sender_example' # str | Email address of the sender. (optional)
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Maximum time period that can be selected is one month. (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. (optional)
limit = 100 # int | Number of documents returned per page (optional) (default to 100)
offset = 0 # int | Index of the first document on the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation (optional) (default to desc)

try:
    # Get the list of all the events for the received emails.
    api_response = api_instance.get_inbound_email_events(sender=sender, start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundParsingApi->get_inbound_email_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender** | **str**| Email address of the sender. | [optional] 
 **start_date** | **date**| Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Maximum time period that can be selected is one month. | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. | [optional] 
 **limit** | **int**| Number of documents returned per page | [optional] [default to 100]
 **offset** | **int**| Index of the first document on the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation | [optional] [default to desc]

### Return type

[**GetInboundEmailEvents**](GetInboundEmailEvents.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_email_events_by_uuid**
> GetInboundEmailEventsByUuid get_inbound_email_events_by_uuid(uuid)

Fetch all events history for one particular received email.

This endpoint will show the list of all events history for one particular received email.

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
api_instance = sib_api_v3_sdk.InboundParsingApi(sib_api_v3_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID to fetch events specific to recieved email

try:
    # Fetch all events history for one particular received email.
    api_response = api_instance.get_inbound_email_events_by_uuid(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundParsingApi->get_inbound_email_events_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID to fetch events specific to recieved email | 

### Return type

[**GetInboundEmailEventsByUuid**](GetInboundEmailEventsByUuid.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

