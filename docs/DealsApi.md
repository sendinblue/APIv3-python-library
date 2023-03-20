# sib_api_v3_sdk.DealsApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crm_attributes_deals_get**](DealsApi.md#crm_attributes_deals_get) | **GET** /crm/attributes/deals | Get deal attributes
[**crm_deals_get**](DealsApi.md#crm_deals_get) | **GET** /crm/deals | Get all deals
[**crm_deals_id_delete**](DealsApi.md#crm_deals_id_delete) | **DELETE** /crm/deals/{id} | Delete a deal
[**crm_deals_id_get**](DealsApi.md#crm_deals_id_get) | **GET** /crm/deals/{id} | Get a deal
[**crm_deals_id_patch**](DealsApi.md#crm_deals_id_patch) | **PATCH** /crm/deals/{id} | Update a deal
[**crm_deals_link_unlink_id_patch**](DealsApi.md#crm_deals_link_unlink_id_patch) | **PATCH** /crm/deals/link-unlink/{id} | Link and Unlink a deal with contacts and companies
[**crm_deals_post**](DealsApi.md#crm_deals_post) | **POST** /crm/deals | Create a deal
[**crm_pipeline_details_get**](DealsApi.md#crm_pipeline_details_get) | **GET** /crm/pipeline/details | Get pipeline stages


# **crm_attributes_deals_get**
> DealAttributes crm_attributes_deals_get()

Get deal attributes

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))

try:
    # Get deal attributes
    api_response = api_instance.crm_attributes_deals_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealsApi->crm_attributes_deals_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DealAttributes**](DealAttributes.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_deals_get**
> DealsList crm_deals_get(filters_attributes=filters_attributes, filters_linked_companies_ids=filters_linked_companies_ids, filters_linked_contacts_ids=filters_linked_contacts_ids, offset=offset, limit=limit, sort=sort, sort_by=sort_by)

Get all deals

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))
filters_attributes = 'filters_attributes_example' # str | Filter by attrbutes. If you have filter for owner on your side please send it as `attributes.owner`.\" (optional)
filters_linked_companies_ids = 'filters_linked_companies_ids_example' # str | Filter by linked companies ids (optional)
filters_linked_contacts_ids = 'filters_linked_contacts_ids_example' # str | Filter by linked companies ids (optional)
offset = 789 # int | Index of the first document of the page (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
sort = 'sort_example' # str | Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed (optional)
sort_by = 'sort_by_example' # str | The field used to sort field names. (optional)

try:
    # Get all deals
    api_response = api_instance.crm_deals_get(filters_attributes=filters_attributes, filters_linked_companies_ids=filters_linked_companies_ids, filters_linked_contacts_ids=filters_linked_contacts_ids, offset=offset, limit=limit, sort=sort, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealsApi->crm_deals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters_attributes** | **str**| Filter by attrbutes. If you have filter for owner on your side please send it as &#x60;attributes.owner&#x60;.\&quot; | [optional] 
 **filters_linked_companies_ids** | **str**| Filter by linked companies ids | [optional] 
 **filters_linked_contacts_ids** | **str**| Filter by linked companies ids | [optional] 
 **offset** | **int**| Index of the first document of the page | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **sort** | **str**| Sort the results in the ascending/descending order. Default order is **descending** by creation if &#x60;sort&#x60; is not passed | [optional] 
 **sort_by** | **str**| The field used to sort field names. | [optional] 

### Return type

[**DealsList**](DealsList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_deals_id_delete**
> crm_deals_id_delete(id)

Delete a deal

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a deal
    api_instance.crm_deals_id_delete(id)
except ApiException as e:
    print("Exception when calling DealsApi->crm_deals_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_deals_id_get**
> Deal crm_deals_id_get(id)

Get a deal

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a deal
    api_response = api_instance.crm_deals_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealsApi->crm_deals_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Deal**](Deal.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_deals_id_patch**
> crm_deals_id_patch(id, body)

Update a deal

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = sib_api_v3_sdk.Body4() # Body4 | Updated deal details.

try:
    # Update a deal
    api_instance.crm_deals_id_patch(id, body)
except ApiException as e:
    print("Exception when calling DealsApi->crm_deals_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body4**](Body4.md)| Updated deal details. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_deals_link_unlink_id_patch**
> crm_deals_link_unlink_id_patch(id, body)

Link and Unlink a deal with contacts and companies

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = sib_api_v3_sdk.Body5() # Body5 | Linked / Unlinked contacts and companies ids.

try:
    # Link and Unlink a deal with contacts and companies
    api_instance.crm_deals_link_unlink_id_patch(id, body)
except ApiException as e:
    print("Exception when calling DealsApi->crm_deals_link_unlink_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body5**](Body5.md)| Linked / Unlinked contacts and companies ids. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_deals_post**
> InlineResponse201 crm_deals_post(body)

Create a deal

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.Body3() # Body3 | Deal create data.

try:
    # Create a deal
    api_response = api_instance.crm_deals_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealsApi->crm_deals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| Deal create data. | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_pipeline_details_get**
> Pipeline crm_pipeline_details_get()

Get pipeline stages

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
api_instance = sib_api_v3_sdk.DealsApi(sib_api_v3_sdk.ApiClient(configuration))

try:
    # Get pipeline stages
    api_response = api_instance.crm_pipeline_details_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealsApi->crm_pipeline_details_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

