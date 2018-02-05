# sib_api_v3_sdk.SendersApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sender**](SendersApi.md#create_sender) | **POST** /senders | Create a new sender
[**delete_sender**](SendersApi.md#delete_sender) | **DELETE** /senders/{senderId} | Delete a sender
[**get_ips**](SendersApi.md#get_ips) | **GET** /senders/ips | Return all the dedicated IPs for your account
[**get_ips_from_sender**](SendersApi.md#get_ips_from_sender) | **GET** /senders/{senderId}/ips | Return all the dedicated IPs for a sender
[**get_senders**](SendersApi.md#get_senders) | **GET** /senders | Get the list of all your senders
[**update_sender**](SendersApi.md#update_sender) | **PUT** /senders/{senderId} | Update a sender


# **create_sender**
> CreateSenderModel create_sender(sender=sender)

Create a new sender

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

# create an instance of the API class
api_instance = sib_api_v3_sdk.SendersApi(sib_api_v3_sdk.ApiClient(configuration))
sender = sib_api_v3_sdk.CreateSender() # CreateSender | sender's name (optional)

try:
    # Create a new sender
    api_response = api_instance.create_sender(sender=sender)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendersApi->create_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender** | [**CreateSender**](CreateSender.md)| sender&#39;s name | [optional] 

### Return type

[**CreateSenderModel**](CreateSenderModel.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sender**
> delete_sender(sender_id)

Delete a sender

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

# create an instance of the API class
api_instance = sib_api_v3_sdk.SendersApi(sib_api_v3_sdk.ApiClient(configuration))
sender_id = 789 # int | Id of the sender

try:
    # Delete a sender
    api_instance.delete_sender(sender_id)
except ApiException as e:
    print("Exception when calling SendersApi->delete_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_id** | **int**| Id of the sender | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ips**
> GetIps get_ips()

Return all the dedicated IPs for your account

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

# create an instance of the API class
api_instance = sib_api_v3_sdk.SendersApi(sib_api_v3_sdk.ApiClient(configuration))

try:
    # Return all the dedicated IPs for your account
    api_response = api_instance.get_ips()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendersApi->get_ips: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetIps**](GetIps.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ips_from_sender**
> GetIpsFromSender get_ips_from_sender(sender_id)

Return all the dedicated IPs for a sender

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

# create an instance of the API class
api_instance = sib_api_v3_sdk.SendersApi(sib_api_v3_sdk.ApiClient(configuration))
sender_id = 789 # int | Id of the sender

try:
    # Return all the dedicated IPs for a sender
    api_response = api_instance.get_ips_from_sender(sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendersApi->get_ips_from_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_id** | **int**| Id of the sender | 

### Return type

[**GetIpsFromSender**](GetIpsFromSender.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_senders**
> GetSendersList get_senders(ip=ip, domain=domain)

Get the list of all your senders

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

# create an instance of the API class
api_instance = sib_api_v3_sdk.SendersApi(sib_api_v3_sdk.ApiClient(configuration))
ip = 'ip_example' # str | Filter your senders for a specific ip (available for dedicated IP usage only) (optional)
domain = 'domain_example' # str | Filter your senders for a specific domain (optional)

try:
    # Get the list of all your senders
    api_response = api_instance.get_senders(ip=ip, domain=domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendersApi->get_senders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Filter your senders for a specific ip (available for dedicated IP usage only) | [optional] 
 **domain** | **str**| Filter your senders for a specific domain | [optional] 

### Return type

[**GetSendersList**](GetSendersList.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sender**
> update_sender(sender_id, sender=sender)

Update a sender

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

# create an instance of the API class
api_instance = sib_api_v3_sdk.SendersApi(sib_api_v3_sdk.ApiClient(configuration))
sender_id = 789 # int | Id of the sender
sender = sib_api_v3_sdk.UpdateSender() # UpdateSender | sender's name (optional)

try:
    # Update a sender
    api_instance.update_sender(sender_id, sender=sender)
except ApiException as e:
    print("Exception when calling SendersApi->update_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_id** | **int**| Id of the sender | 
 **sender** | [**UpdateSender**](UpdateSender.md)| sender&#39;s name | [optional] 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

