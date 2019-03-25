# sib_api_v3_sdk.TransactionalSMSApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sms_events**](TransactionalSMSApi.md#get_sms_events) | **GET** /transactionalSMS/statistics/events | Get all the SMS activity (unaggregated events)
[**get_transac_aggregated_sms_report**](TransactionalSMSApi.md#get_transac_aggregated_sms_report) | **GET** /transactionalSMS/statistics/aggregatedReport | Get your SMS activity aggregated over a period of time
[**get_transac_sms_report**](TransactionalSMSApi.md#get_transac_sms_report) | **GET** /transactionalSMS/statistics/reports | Get your SMS activity aggregated per day
[**send_transac_sms**](TransactionalSMSApi.md#send_transac_sms) | **POST** /transactionalSMS/sms | Send the SMS campaign to the specified mobile number

# **get_sms_events**
> GetSmsEventReport get_sms_events(limit=limit, start_date=start_date, end_date=end_date, offset=offset, days=days, phone_number=phone_number, event=event, tags=tags)

Get all the SMS activity (unaggregated events)

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
api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
limit = 56 # int | Number of documents per page (optional)
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report (optional)
offset = 56 # int | Index of the first document of the page (optional)
days = 56 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
phone_number = 'phone_number_example' # str | Filter the report for a specific phone number (optional)
event = 'event_example' # str | Filter the report for specific events (optional)
tags = 'tags_example' # str | Filter the report for specific tags passed as a serialized urlencoded array (optional)

try:
    # Get all the SMS activity (unaggregated events)
    api_response = api_instance.get_sms_events(limit=limit, start_date=start_date, end_date=end_date, offset=offset, days=days, phone_number=phone_number, event=event, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalSMSApi->get_sms_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**int**](.md)| Number of documents per page | [optional] 
 **start_date** | [**str**](.md)| Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report | [optional] 
 **end_date** | [**str**](.md)| Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report | [optional] 
 **offset** | [**int**](.md)| Index of the first document of the page | [optional] 
 **days** | [**int**](.md)| Number of days in the past including today (positive integer). Not compatible with &#x27;startDate&#x27; and &#x27;endDate&#x27; | [optional] 
 **phone_number** | [**str**](.md)| Filter the report for a specific phone number | [optional] 
 **event** | [**str**](.md)| Filter the report for specific events | [optional] 
 **tags** | [**str**](.md)| Filter the report for specific tags passed as a serialized urlencoded array | [optional] 

### Return type

[**GetSmsEventReport**](GetSmsEventReport.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transac_aggregated_sms_report**
> GetTransacAggregatedSmsReport get_transac_aggregated_sms_report(start_date=start_date, end_date=end_date, days=days, tag=tag)

Get your SMS activity aggregated over a period of time

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
api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report (optional)
days = 56 # int | Number of days in the past including today (positive integer). Not compatible with startDate and endDate (optional)
tag = 'tag_example' # str | Filter on a tag (optional)

try:
    # Get your SMS activity aggregated over a period of time
    api_response = api_instance.get_transac_aggregated_sms_report(start_date=start_date, end_date=end_date, days=days, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalSMSApi->get_transac_aggregated_sms_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | [**str**](.md)| Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report | [optional] 
 **end_date** | [**str**](.md)| Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report | [optional] 
 **days** | [**int**](.md)| Number of days in the past including today (positive integer). Not compatible with startDate and endDate | [optional] 
 **tag** | [**str**](.md)| Filter on a tag | [optional] 

### Return type

[**GetTransacAggregatedSmsReport**](GetTransacAggregatedSmsReport.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transac_sms_report**
> GetTransacSmsReport get_transac_sms_report(start_date=start_date, end_date=end_date, days=days, tag=tag)

Get your SMS activity aggregated per day

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
api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report (optional)
days = 56 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
tag = 'tag_example' # str | Filter on a tag (optional)

try:
    # Get your SMS activity aggregated per day
    api_response = api_instance.get_transac_sms_report(start_date=start_date, end_date=end_date, days=days, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalSMSApi->get_transac_sms_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | [**str**](.md)| Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report | [optional] 
 **end_date** | [**str**](.md)| Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report | [optional] 
 **days** | [**int**](.md)| Number of days in the past including today (positive integer). Not compatible with &#x27;startDate&#x27; and &#x27;endDate&#x27; | [optional] 
 **tag** | [**str**](.md)| Filter on a tag | [optional] 

### Return type

[**GetTransacSmsReport**](GetTransacSmsReport.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_transac_sms**
> SendSms send_transac_sms(body)

Send the SMS campaign to the specified mobile number

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
api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.SendTransacSms() # SendTransacSms | Values to send a transactional SMS

try:
    # Send the SMS campaign to the specified mobile number
    api_response = api_instance.send_transac_sms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalSMSApi->send_transac_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendTransacSms**](SendTransacSms.md)| Values to send a transactional SMS | 

### Return type

[**SendSms**](SendSms.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

