# sib_api_v3_sdk.AttributesApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute**](AttributesApi.md#create_attribute) | **POST** /contacts/attributes | Creates contact attributes
[**delete_attribute**](AttributesApi.md#delete_attribute) | **DELETE** /contacts/attributes/{attributeId} | Deletes an attribute
[**get_attributes**](AttributesApi.md#get_attributes) | **GET** /contacts/attributes | Lists all attributes


# **create_attribute**
> CreateModel create_attribute(create_attribute)

Creates contact attributes

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
api_instance = sib_api_v3_sdk.AttributesApi()
create_attribute = sib_api_v3_sdk.CreateAttribute() # CreateAttribute | Values to create an attribute

try: 
    # Creates contact attributes
    api_response = api_instance.create_attribute(create_attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_attribute** | [**CreateAttribute**](CreateAttribute.md)| Values to create an attribute | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute**
> delete_attribute(attribute_id)

Deletes an attribute

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
api_instance = sib_api_v3_sdk.AttributesApi()
attribute_id = 789 # int | id of the attribute

try: 
    # Deletes an attribute
    api_instance.delete_attribute(attribute_id)
except ApiException as e:
    print("Exception when calling AttributesApi->delete_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **int**| id of the attribute | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> GetAttributes get_attributes()

Lists all attributes

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
api_instance = sib_api_v3_sdk.AttributesApi()

try: 
    # Lists all attributes
    api_response = api_instance.get_attributes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAttributes**](GetAttributes.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

