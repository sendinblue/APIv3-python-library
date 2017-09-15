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
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalSMSApi()
limit = 50 # int | Number of documents per page (optional) (default to 50)
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report (optional)
offset = 0 # int | Index of the first document of the page (optional) (default to 0)
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
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **start_date** | **date**| Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report | [optional] 
 **offset** | **int**| Index of the first document of the page | [optional] [default to 0]
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **phone_number** | **str**| Filter the report for a specific phone number | [optional] 
 **event** | **str**| Filter the report for specific events | [optional] 
 **tags** | **str**| Filter the report for specific tags passed as a serialized urlencoded array | [optional] 

### Return type

[**GetSmsEventReport**](GetSmsEventReport.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
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
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalSMSApi()
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report (optional)
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
 **start_date** | **date**| Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with startDate and endDate | [optional] 
 **tag** | **str**| Filter on a tag | [optional] 

### Return type

[**GetTransacAggregatedSmsReport**](GetTransacAggregatedSmsReport.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
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
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalSMSApi()
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report (optional)
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
 **start_date** | **date**| Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **tag** | **str**| Filter on a tag | [optional] 

### Return type

[**GetTransacSmsReport**](GetTransacSmsReport.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_transac_sms**
> SendSms send_transac_sms(send_transac_sms)

Send the SMS campaign to the specified mobile number

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
api_instance = sib_api_v3_sdk.TransactionalSMSApi()
send_transac_sms = sib_api_v3_sdk.SendTransacSms() # SendTransacSms | Values to send a transactional SMS

try: 
    # Send the SMS campaign to the specified mobile number
    api_response = api_instance.send_transac_sms(send_transac_sms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalSMSApi->send_transac_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_transac_sms** | [**SendTransacSms**](SendTransacSms.md)| Values to send a transactional SMS | 

### Return type

[**SendSms**](SendSms.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

