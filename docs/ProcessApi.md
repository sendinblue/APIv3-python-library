# sib_api_v3_sdk.ProcessApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_process**](ProcessApi.md#get_process) | **GET** /processes/{processId} | Return the informations for a process
[**get_processes**](ProcessApi.md#get_processes) | **GET** /processes | Return all the processes for your account

# **get_process**
> GetProcess get_process(process_id)

Return the informations for a process

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
api_instance = sib_api_v3_sdk.ProcessApi(sib_api_v3_sdk.ApiClient(configuration))
process_id = 56 # int | Id of the process

try:
    # Return the informations for a process
    api_response = api_instance.get_process(process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | [**int**](.md)| Id of the process | 

### Return type

[**GetProcess**](GetProcess.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_processes**
> GetProcesses get_processes(limit=limit, offset=offset)

Return all the processes for your account

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
api_instance = sib_api_v3_sdk.ProcessApi(sib_api_v3_sdk.ApiClient(configuration))
limit = 56 # int | Number limitation for the result returned (optional)
offset = 56 # int | Beginning point in the list to retrieve from. (optional)

try:
    # Return all the processes for your account
    api_response = api_instance.get_processes(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_processes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**int**](.md)| Number limitation for the result returned | [optional] 
 **offset** | [**int**](.md)| Beginning point in the list to retrieve from. | [optional] 

### Return type

[**GetProcesses**](GetProcesses.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

