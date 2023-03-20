# sib_api_v3_sdk.FilesApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crm_files_get**](FilesApi.md#crm_files_get) | **GET** /crm/files | Get all files
[**crm_files_id_data_get**](FilesApi.md#crm_files_id_data_get) | **GET** /crm/files/{id}/data | Get file details
[**crm_files_id_delete**](FilesApi.md#crm_files_id_delete) | **DELETE** /crm/files/{id} | Delete a file
[**crm_files_id_get**](FilesApi.md#crm_files_id_get) | **GET** /crm/files/{id} | Download a file
[**crm_files_post**](FilesApi.md#crm_files_post) | **POST** /crm/files | Upload a file


# **crm_files_get**
> FileList crm_files_get(entity=entity, entity_ids=entity_ids, date_from=date_from, date_to=date_to, offset=offset, limit=limit, sort=sort)

Get all files

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
api_instance = sib_api_v3_sdk.FilesApi(sib_api_v3_sdk.ApiClient(configuration))
entity = 'entity_example' # str | Filter by file entity type (optional)
entity_ids = 'entity_ids_example' # str | Filter by file entity IDs (optional)
date_from = 56 # int | dateFrom to date range filter type (timestamp in milliseconds) (optional)
date_to = 56 # int | dateTo to date range filter type (timestamp in milliseconds) (optional)
offset = 789 # int | Index of the first document of the page (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
sort = 'sort_example' # str | Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed (optional)

try:
    # Get all files
    api_response = api_instance.crm_files_get(entity=entity, entity_ids=entity_ids, date_from=date_from, date_to=date_to, offset=offset, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->crm_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| Filter by file entity type | [optional] 
 **entity_ids** | **str**| Filter by file entity IDs | [optional] 
 **date_from** | **int**| dateFrom to date range filter type (timestamp in milliseconds) | [optional] 
 **date_to** | **int**| dateTo to date range filter type (timestamp in milliseconds) | [optional] 
 **offset** | **int**| Index of the first document of the page | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **sort** | **str**| Sort the results in the ascending/descending order. Default order is **descending** by creation if &#x60;sort&#x60; is not passed | [optional] 

### Return type

[**FileList**](FileList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_files_id_data_get**
> FileData crm_files_id_data_get(id)

Get file details

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
api_instance = sib_api_v3_sdk.FilesApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | File id to get file data.

try:
    # Get file details
    api_response = api_instance.crm_files_id_data_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->crm_files_id_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File id to get file data. | 

### Return type

[**FileData**](FileData.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_files_id_delete**
> crm_files_id_delete(id)

Delete a file

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
api_instance = sib_api_v3_sdk.FilesApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | File id to delete.

try:
    # Delete a file
    api_instance.crm_files_id_delete(id)
except ApiException as e:
    print("Exception when calling FilesApi->crm_files_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File id to delete. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_files_id_get**
> FileDownloadableLink crm_files_id_get(id)

Download a file

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
api_instance = sib_api_v3_sdk.FilesApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | File id to download.

try:
    # Download a file
    api_response = api_instance.crm_files_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->crm_files_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File id to download. | 

### Return type

[**FileDownloadableLink**](FileDownloadableLink.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_files_post**
> FileData crm_files_post(file, deal_id=deal_id, contact_id=contact_id, company_id=company_id)

Upload a file

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
api_instance = sib_api_v3_sdk.FilesApi(sib_api_v3_sdk.ApiClient(configuration))
file = '/path/to/file.txt' # file | File data to create a file.
deal_id = 'deal_id_example' # str | Deal id linked to a file (optional)
contact_id = 789 # int | Contact id linked to a file (optional)
company_id = 'company_id_example' # str | Company id linked to a file (optional)

try:
    # Upload a file
    api_response = api_instance.crm_files_post(file, deal_id=deal_id, contact_id=contact_id, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->crm_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File data to create a file. | 
 **deal_id** | **str**| Deal id linked to a file | [optional] 
 **contact_id** | **int**| Contact id linked to a file | [optional] 
 **company_id** | **str**| Company id linked to a file | [optional] 

### Return type

[**FileData**](FileData.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

