# sib_api_v3_sdk.TransactionalWhatsAppApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_whatsapp_event_report**](TransactionalWhatsAppApi.md#get_whatsapp_event_report) | **GET** /whatsapp/statistics/events | Get all your WhatsApp activity (unaggregated events)
[**send_whatsapp_message**](TransactionalWhatsAppApi.md#send_whatsapp_message) | **POST** /whatsapp/sendMessage | Send a WhatsApp message


# **get_whatsapp_event_report**
> GetWhatsappEventReport get_whatsapp_event_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, contact_number=contact_number, event=event, sort=sort)

Get all your WhatsApp activity (unaggregated events)

This endpoint will show the unaggregated statistics for WhatsApp activity (30 days by default if `startDate` and `endDate` or `days` is not passed. The date range can not exceed 90 days)

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
api_instance = sib_api_v3_sdk.TransactionalWhatsAppApi(sib_api_v3_sdk.ApiClient(configuration))
limit = 2500 # int | Number limitation for the result returned (optional) (default to 2500)
offset = 0 # int | Beginning point in the list to retrieve from (optional) (default to 0)
start_date = 'start_date_example' # str | **Mandatory if endDate is used.** Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate  (optional)
end_date = 'end_date_example' # str | **Mandatory if startDate is used.** Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate  (optional)
days = 789 # int | Number of days in the past including today (positive integer). _Not compatible with 'startDate' and 'endDate'_  (optional)
contact_number = 'contact_number_example' # str | Filter results for specific contact (WhatsApp Number with country code. Example, 85264318721) (optional)
event = 'event_example' # str | Filter the report for a specific event type (optional)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Get all your WhatsApp activity (unaggregated events)
    api_response = api_instance.get_whatsapp_event_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, contact_number=contact_number, event=event, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalWhatsAppApi->get_whatsapp_event_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number limitation for the result returned | [optional] [default to 2500]
 **offset** | **int**| Beginning point in the list to retrieve from | [optional] [default to 0]
 **start_date** | **str**| **Mandatory if endDate is used.** Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate  | [optional] 
 **end_date** | **str**| **Mandatory if startDate is used.** Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate  | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). _Not compatible with &#39;startDate&#39; and &#39;endDate&#39;_  | [optional] 
 **contact_number** | **str**| Filter results for specific contact (WhatsApp Number with country code. Example, 85264318721) | [optional] 
 **event** | **str**| Filter the report for a specific event type | [optional] 
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetWhatsappEventReport**](GetWhatsappEventReport.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_whatsapp_message**
> InlineResponse2012 send_whatsapp_message(send_whatsapp_message)

Send a WhatsApp message

This endpoint is used to send a WhatsApp message. <br/>(**The first message you send using the API must contain a Template ID. You must create a template on WhatsApp on the Sendinblue platform to fetch the Template ID.**)

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
api_instance = sib_api_v3_sdk.TransactionalWhatsAppApi(sib_api_v3_sdk.ApiClient(configuration))
send_whatsapp_message = sib_api_v3_sdk.SendWhatsappMessage() # SendWhatsappMessage | Values to send WhatsApp message

try:
    # Send a WhatsApp message
    api_response = api_instance.send_whatsapp_message(send_whatsapp_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalWhatsAppApi->send_whatsapp_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_whatsapp_message** | [**SendWhatsappMessage**](SendWhatsappMessage.md)| Values to send WhatsApp message | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

