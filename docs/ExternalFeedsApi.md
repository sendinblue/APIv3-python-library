# sib_api_v3_sdk.ExternalFeedsApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_feed**](ExternalFeedsApi.md#create_external_feed) | **POST** /feeds | Create an external feed
[**delete_external_feed**](ExternalFeedsApi.md#delete_external_feed) | **DELETE** /feeds/{uuid} | Delete an external feed
[**get_all_external_feeds**](ExternalFeedsApi.md#get_all_external_feeds) | **GET** /feeds | Fetch all external feeds
[**get_external_feed_by_uuid**](ExternalFeedsApi.md#get_external_feed_by_uuid) | **GET** /feeds/{uuid} | Get an external feed by UUID
[**update_external_feed**](ExternalFeedsApi.md#update_external_feed) | **PUT** /feeds/{uuid} | Update an external feed


# **create_external_feed**
> InlineResponse2013 create_external_feed(create_external_feed)

Create an external feed

This endpoint will create an external feed.

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
api_instance = sib_api_v3_sdk.ExternalFeedsApi(sib_api_v3_sdk.ApiClient(configuration))
create_external_feed = sib_api_v3_sdk.CreateExternalFeed() # CreateExternalFeed | Values to create a feed

try:
    # Create an external feed
    api_response = api_instance.create_external_feed(create_external_feed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalFeedsApi->create_external_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_feed** | [**CreateExternalFeed**](CreateExternalFeed.md)| Values to create a feed | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_feed**
> delete_external_feed(uuid)

Delete an external feed

This endpoint will delete an external feed.

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
api_instance = sib_api_v3_sdk.ExternalFeedsApi(sib_api_v3_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the feed to delete

try:
    # Delete an external feed
    api_instance.delete_external_feed(uuid)
except ApiException as e:
    print("Exception when calling ExternalFeedsApi->delete_external_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the feed to delete | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_external_feeds**
> GetAllExternalFeeds get_all_external_feeds(search=search, start_date=start_date, end_date=end_date, sort=sort, auth_type=auth_type, limit=limit, offset=offset)

Fetch all external feeds

This endpoint can fetch all created external feeds.

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
api_instance = sib_api_v3_sdk.ExternalFeedsApi(sib_api_v3_sdk.ApiClient(configuration))
search = 'search_example' # str | Can be used to filter records by search keyword on feed name (optional)
start_date = '2013-10-20' # date | Mandatory if `endDate` is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Can be maximum 30 days older than current date. (optional)
end_date = '2013-10-20' # date | Mandatory if `startDate` is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. (optional)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed. (optional) (default to desc)
auth_type = 'auth_type_example' # str | Filter the records by `authType` of the feed. (optional)
limit = 50 # int | Number of documents returned per page. (optional) (default to 50)
offset = 0 # int | Index of the first document on the page. (optional) (default to 0)

try:
    # Fetch all external feeds
    api_response = api_instance.get_all_external_feeds(search=search, start_date=start_date, end_date=end_date, sort=sort, auth_type=auth_type, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalFeedsApi->get_all_external_feeds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Can be used to filter records by search keyword on feed name | [optional] 
 **start_date** | **date**| Mandatory if &#x60;endDate&#x60; is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Can be maximum 30 days older than current date. | [optional] 
 **end_date** | **date**| Mandatory if &#x60;startDate&#x60; is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. | [optional] 
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed. | [optional] [default to desc]
 **auth_type** | **str**| Filter the records by &#x60;authType&#x60; of the feed. | [optional] 
 **limit** | **int**| Number of documents returned per page. | [optional] [default to 50]
 **offset** | **int**| Index of the first document on the page. | [optional] [default to 0]

### Return type

[**GetAllExternalFeeds**](GetAllExternalFeeds.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_feed_by_uuid**
> GetExternalFeedByUUID get_external_feed_by_uuid(uuid)

Get an external feed by UUID

This endpoint will update an external feed.

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
api_instance = sib_api_v3_sdk.ExternalFeedsApi(sib_api_v3_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the feed to fetch

try:
    # Get an external feed by UUID
    api_response = api_instance.get_external_feed_by_uuid(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalFeedsApi->get_external_feed_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the feed to fetch | 

### Return type

[**GetExternalFeedByUUID**](GetExternalFeedByUUID.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_feed**
> update_external_feed(uuid, update_external_feed)

Update an external feed

This endpoint will update an external feed.

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
api_instance = sib_api_v3_sdk.ExternalFeedsApi(sib_api_v3_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the feed to update
update_external_feed = sib_api_v3_sdk.UpdateExternalFeed() # UpdateExternalFeed | Values to update a feed

try:
    # Update an external feed
    api_instance.update_external_feed(uuid, update_external_feed)
except ApiException as e:
    print("Exception when calling ExternalFeedsApi->update_external_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the feed to update | 
 **update_external_feed** | [**UpdateExternalFeed**](UpdateExternalFeed.md)| Values to update a feed | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

