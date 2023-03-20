# sib_api_v3_sdk.ConversationsApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversations_agent_online_ping_post**](ConversationsApi.md#conversations_agent_online_ping_post) | **POST** /conversations/agentOnlinePing | Sets agent’s status to online for 2-3 minutes
[**conversations_messages_id_delete**](ConversationsApi.md#conversations_messages_id_delete) | **DELETE** /conversations/messages/{id} | Delete a message sent by an agent
[**conversations_messages_id_get**](ConversationsApi.md#conversations_messages_id_get) | **GET** /conversations/messages/{id} | Get a message
[**conversations_messages_id_put**](ConversationsApi.md#conversations_messages_id_put) | **PUT** /conversations/messages/{id} | Update a message sent by an agent
[**conversations_messages_post**](ConversationsApi.md#conversations_messages_post) | **POST** /conversations/messages | Send a message as an agent
[**conversations_pushed_messages_id_delete**](ConversationsApi.md#conversations_pushed_messages_id_delete) | **DELETE** /conversations/pushedMessages/{id} | Delete an automated message
[**conversations_pushed_messages_id_get**](ConversationsApi.md#conversations_pushed_messages_id_get) | **GET** /conversations/pushedMessages/{id} | Get an automated message
[**conversations_pushed_messages_id_put**](ConversationsApi.md#conversations_pushed_messages_id_put) | **PUT** /conversations/pushedMessages/{id} | Update an automated message
[**conversations_pushed_messages_post**](ConversationsApi.md#conversations_pushed_messages_post) | **POST** /conversations/pushedMessages | Send an automated message to a visitor


# **conversations_agent_online_ping_post**
> conversations_agent_online_ping_post(body)

Sets agent’s status to online for 2-3 minutes

We recommend pinging this endpoint every minute for as long as the agent has to be considered online.

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.Body12() # Body12 | Agent fields.

try:
    # Sets agent’s status to online for 2-3 minutes
    api_instance.conversations_agent_online_ping_post(body)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_agent_online_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body12**](Body12.md)| Agent fields. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_messages_id_delete**
> conversations_messages_id_delete(id)

Delete a message sent by an agent

Only agents’ messages can be deleted.

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | ID of the message

try:
    # Delete a message sent by an agent
    api_instance.conversations_messages_id_delete(id)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_messages_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the message | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_messages_id_get**
> ConversationsMessage conversations_messages_id_get(id)

Get a message

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | ID of the message

try:
    # Get a message
    api_response = api_instance.conversations_messages_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_messages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the message | 

### Return type

[**ConversationsMessage**](ConversationsMessage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_messages_id_put**
> ConversationsMessage conversations_messages_id_put(id, body=body)

Update a message sent by an agent

Only agents’ messages can be edited.

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | ID of the message
body = sib_api_v3_sdk.Body9() # Body9 |  (optional)

try:
    # Update a message sent by an agent
    api_response = api_instance.conversations_messages_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_messages_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the message | 
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

[**ConversationsMessage**](ConversationsMessage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_messages_post**
> ConversationsMessage conversations_messages_post(body)

Send a message as an agent

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.Body8() # Body8 | Message fields.

try:
    # Send a message as an agent
    api_response = api_instance.conversations_messages_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_messages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body8**](Body8.md)| Message fields. | 

### Return type

[**ConversationsMessage**](ConversationsMessage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_pushed_messages_id_delete**
> conversations_pushed_messages_id_delete(id)

Delete an automated message

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | ID of the message

try:
    # Delete an automated message
    api_instance.conversations_pushed_messages_id_delete(id)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_pushed_messages_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the message | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_pushed_messages_id_get**
> ConversationsMessage conversations_pushed_messages_id_get(id)

Get an automated message

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | ID of the message sent previously

try:
    # Get an automated message
    api_response = api_instance.conversations_pushed_messages_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_pushed_messages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the message sent previously | 

### Return type

[**ConversationsMessage**](ConversationsMessage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_pushed_messages_id_put**
> ConversationsMessage conversations_pushed_messages_id_put(id, body)

Update an automated message

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | ID of the message
body = sib_api_v3_sdk.Body11() # Body11 | 

try:
    # Update an automated message
    api_response = api_instance.conversations_pushed_messages_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_pushed_messages_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the message | 
 **body** | [**Body11**](Body11.md)|  | 

### Return type

[**ConversationsMessage**](ConversationsMessage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_pushed_messages_post**
> ConversationsMessage conversations_pushed_messages_post(body)

Send an automated message to a visitor

Example of automated messages: order status, announce new features in your web app, etc.

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
api_instance = sib_api_v3_sdk.ConversationsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.Body10() # Body10 | 

try:
    # Send an automated message to a visitor
    api_response = api_instance.conversations_pushed_messages_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversations_pushed_messages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body10**](Body10.md)|  | 

### Return type

[**ConversationsMessage**](ConversationsMessage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

