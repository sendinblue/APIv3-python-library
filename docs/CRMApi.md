# sib_api_v3_sdk.CRMApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crm_notes_get**](CRMApi.md#crm_notes_get) | **GET** /crm/notes | Get all notes
[**crm_notes_id_delete**](CRMApi.md#crm_notes_id_delete) | **DELETE** /crm/notes/{id} | Delete a note
[**crm_notes_id_get**](CRMApi.md#crm_notes_id_get) | **GET** /crm/notes/{id} | Get a note
[**crm_notes_id_patch**](CRMApi.md#crm_notes_id_patch) | **PATCH** /crm/notes/{id} | Update a note
[**crm_notes_post**](CRMApi.md#crm_notes_post) | **POST** /crm/notes | Create a note
[**crm_tasks_get**](CRMApi.md#crm_tasks_get) | **GET** /crm/tasks | Get all tasks
[**crm_tasks_id_delete**](CRMApi.md#crm_tasks_id_delete) | **DELETE** /crm/tasks/{id} | Delete a task
[**crm_tasks_id_get**](CRMApi.md#crm_tasks_id_get) | **GET** /crm/tasks/{id} | Get a task
[**crm_tasks_id_patch**](CRMApi.md#crm_tasks_id_patch) | **PATCH** /crm/tasks/{id} | Update a task
[**crm_tasks_post**](CRMApi.md#crm_tasks_post) | **POST** /crm/tasks | Create a task
[**crm_tasktypes_get**](CRMApi.md#crm_tasktypes_get) | **GET** /crm/tasktypes | Get all task types


# **crm_notes_get**
> NoteList crm_notes_get(entity=entity, entity_ids=entity_ids, date_from=date_from, date_to=date_to, offset=offset, limit=limit, sort=sort)

Get all notes

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
entity = 'entity_example' # str | Filter by note entity type (optional)
entity_ids = 'entity_ids_example' # str | Filter by note entity IDs (optional)
date_from = 56 # int | dateFrom to date range filter type (timestamp in milliseconds) (optional)
date_to = 56 # int | dateTo to date range filter type (timestamp in milliseconds) (optional)
offset = 789 # int | Index of the first document of the page (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
sort = 'sort_example' # str | Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed (optional)

try:
    # Get all notes
    api_response = api_instance.crm_notes_get(entity=entity, entity_ids=entity_ids, date_from=date_from, date_to=date_to, offset=offset, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_notes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| Filter by note entity type | [optional] 
 **entity_ids** | **str**| Filter by note entity IDs | [optional] 
 **date_from** | **int**| dateFrom to date range filter type (timestamp in milliseconds) | [optional] 
 **date_to** | **int**| dateTo to date range filter type (timestamp in milliseconds) | [optional] 
 **offset** | **int**| Index of the first document of the page | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **sort** | **str**| Sort the results in the ascending/descending order. Default order is **descending** by creation if &#x60;sort&#x60; is not passed | [optional] 

### Return type

[**NoteList**](NoteList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_notes_id_delete**
> crm_notes_id_delete(id)

Delete a note

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | Note ID to delete

try:
    # Delete a note
    api_instance.crm_notes_id_delete(id)
except ApiException as e:
    print("Exception when calling CRMApi->crm_notes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Note ID to delete | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_notes_id_get**
> Note crm_notes_id_get(id)

Get a note

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | Note ID to get

try:
    # Get a note
    api_response = api_instance.crm_notes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_notes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Note ID to get | 

### Return type

[**Note**](Note.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_notes_id_patch**
> crm_notes_id_patch(id, body)

Update a note

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | Note ID to update
body = sib_api_v3_sdk.NoteData() # NoteData | Note data to update a note

try:
    # Update a note
    api_instance.crm_notes_id_patch(id, body)
except ApiException as e:
    print("Exception when calling CRMApi->crm_notes_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Note ID to update | 
 **body** | [**NoteData**](NoteData.md)| Note data to update a note | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_notes_post**
> NoteId crm_notes_post(body)

Create a note

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.NoteData() # NoteData | Note data to create a note.

try:
    # Create a note
    api_response = api_instance.crm_notes_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_notes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteData**](NoteData.md)| Note data to create a note. | 

### Return type

[**NoteId**](NoteId.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_tasks_get**
> TaskList crm_tasks_get(filter_type=filter_type, filter_status=filter_status, filter_date=filter_date, filter_assign_to=filter_assign_to, filter_contacts=filter_contacts, filter_deals=filter_deals, filter_companies=filter_companies, date_from=date_from, date_to=date_to, offset=offset, limit=limit, sort=sort, sort_by=sort_by)

Get all tasks

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
filter_type = 'filter_type_example' # str | Filter by task type (ID) (optional)
filter_status = 'filter_status_example' # str | Filter by task status (optional)
filter_date = 'filter_date_example' # str | Filter by date (optional)
filter_assign_to = 'filter_assign_to_example' # str | Filter by assignTo id (optional)
filter_contacts = 'filter_contacts_example' # str | Filter by contact ids (optional)
filter_deals = 'filter_deals_example' # str | Filter by deals ids (optional)
filter_companies = 'filter_companies_example' # str | Filter by companies ids (optional)
date_from = 56 # int | dateFrom to date range filter type (timestamp in milliseconds) (optional)
date_to = 56 # int | dateTo to date range filter type (timestamp in milliseconds) (optional)
offset = 789 # int | Index of the first document of the page (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
sort = 'sort_example' # str | Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed (optional)
sort_by = 'sort_by_example' # str | The field used to sort field names. (optional)

try:
    # Get all tasks
    api_response = api_instance.crm_tasks_get(filter_type=filter_type, filter_status=filter_status, filter_date=filter_date, filter_assign_to=filter_assign_to, filter_contacts=filter_contacts, filter_deals=filter_deals, filter_companies=filter_companies, date_from=date_from, date_to=date_to, offset=offset, limit=limit, sort=sort, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_type** | **str**| Filter by task type (ID) | [optional] 
 **filter_status** | **str**| Filter by task status | [optional] 
 **filter_date** | **str**| Filter by date | [optional] 
 **filter_assign_to** | **str**| Filter by assignTo id | [optional] 
 **filter_contacts** | **str**| Filter by contact ids | [optional] 
 **filter_deals** | **str**| Filter by deals ids | [optional] 
 **filter_companies** | **str**| Filter by companies ids | [optional] 
 **date_from** | **int**| dateFrom to date range filter type (timestamp in milliseconds) | [optional] 
 **date_to** | **int**| dateTo to date range filter type (timestamp in milliseconds) | [optional] 
 **offset** | **int**| Index of the first document of the page | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **sort** | **str**| Sort the results in the ascending/descending order. Default order is **descending** by creation if &#x60;sort&#x60; is not passed | [optional] 
 **sort_by** | **str**| The field used to sort field names. | [optional] 

### Return type

[**TaskList**](TaskList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_tasks_id_delete**
> crm_tasks_id_delete(id)

Delete a task

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a task
    api_instance.crm_tasks_id_delete(id)
except ApiException as e:
    print("Exception when calling CRMApi->crm_tasks_id_delete: %s\n" % e)
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

# **crm_tasks_id_get**
> Task crm_tasks_id_get(id)

Get a task

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a task
    api_response = api_instance.crm_tasks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_tasks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_tasks_id_patch**
> crm_tasks_id_patch(id, body)

Update a task

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = sib_api_v3_sdk.Body1() # Body1 | Updated task details.

try:
    # Update a task
    api_instance.crm_tasks_id_patch(id, body)
except ApiException as e:
    print("Exception when calling CRMApi->crm_tasks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body1**](Body1.md)| Updated task details. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_tasks_post**
> InlineResponse201 crm_tasks_post(body)

Create a task

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.Body() # Body | Task name.

try:
    # Create a task
    api_response = api_instance.crm_tasks_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Task name. | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_tasktypes_get**
> TaskTypes crm_tasktypes_get()

Get all task types

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
api_instance = sib_api_v3_sdk.CRMApi(sib_api_v3_sdk.ApiClient(configuration))

try:
    # Get all task types
    api_response = api_instance.crm_tasktypes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_tasktypes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskTypes**](TaskTypes.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

