# sib_api_v3_sdk.ResellerApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credits**](ResellerApi.md#add_credits) | **POST** /reseller/children/{childAuthKey}/credits/add | Add Email and/or SMS credits to a specific child account
[**associate_ip_to_child**](ResellerApi.md#associate_ip_to_child) | **POST** /reseller/children/{childAuthKey}/ips/associate | Associate a dedicated IP to the child
[**create_child_domain**](ResellerApi.md#create_child_domain) | **POST** /reseller/children/{childAuthKey}/domains | Creates a domain for a child account
[**create_reseller_child**](ResellerApi.md#create_reseller_child) | **POST** /reseller/children | Creates a reseller child
[**delete_child_domain**](ResellerApi.md#delete_child_domain) | **DELETE** /reseller/children/{childAuthKey}/domains/{domainName} | Deletes the sender domain of the reseller child based on the childAuthKey and domainName passed
[**delete_reseller_child**](ResellerApi.md#delete_reseller_child) | **DELETE** /reseller/children/{childAuthKey} | Deletes a single reseller child based on the childAuthKey supplied
[**dissociate_ip_from_child**](ResellerApi.md#dissociate_ip_from_child) | **POST** /reseller/children/{childAuthKey}/ips/dissociate | Dissociate a dedicated IP to the child
[**get_child_account_creation_status**](ResellerApi.md#get_child_account_creation_status) | **GET** /reseller/children/{childAuthKey}/accountCreationStatus | Returns the status of reseller&#39;s child account creation, whether it is successfully created (exists) or not based on the childAuthKey supplied
[**get_child_domains**](ResellerApi.md#get_child_domains) | **GET** /reseller/children/{childAuthKey}/domains | Gets all the sender domains of a specific child account
[**get_child_info**](ResellerApi.md#get_child_info) | **GET** /reseller/children/{childAuthKey} | Gets the info about a specific child account
[**get_reseller_childs**](ResellerApi.md#get_reseller_childs) | **GET** /reseller/children | Gets the list of all reseller&#39;s children accounts
[**get_sso_token**](ResellerApi.md#get_sso_token) | **GET** /reseller/children/{childAuthKey}/auth | Get session token to access Sendinblue (SSO)
[**remove_credits**](ResellerApi.md#remove_credits) | **POST** /reseller/children/{childAuthKey}/credits/remove | Remove Email and/or SMS credits from a specific child account
[**update_child_account_status**](ResellerApi.md#update_child_account_status) | **PUT** /reseller/children/{childAuthKey}/accountStatus | Updates infos of reseller&#39;s child account status based on the childAuthKey supplied
[**update_child_domain**](ResellerApi.md#update_child_domain) | **PUT** /reseller/children/{childAuthKey}/domains/{domainName} | Updates the sender domain of reseller&#39;s child based on the childAuthKey and domainName passed
[**update_reseller_child**](ResellerApi.md#update_reseller_child) | **PUT** /reseller/children/{childAuthKey} | Updates infos of reseller&#39;s child based on the childAuthKey supplied


# **add_credits**
> RemainingCreditModel add_credits(child_auth_key, add_credits)

Add Email and/or SMS credits to a specific child account

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
add_credits = sib_api_v3_sdk.AddCredits() # AddCredits | Values to post to add credit to a specific child account

try:
    # Add Email and/or SMS credits to a specific child account
    api_response = api_instance.add_credits(child_auth_key, add_credits)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->add_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **add_credits** | [**AddCredits**](AddCredits.md)| Values to post to add credit to a specific child account | 

### Return type

[**RemainingCreditModel**](RemainingCreditModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_ip_to_child**
> associate_ip_to_child(child_auth_key, ip)

Associate a dedicated IP to the child

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
ip = sib_api_v3_sdk.ManageIp() # ManageIp | IP to associate

try:
    # Associate a dedicated IP to the child
    api_instance.associate_ip_to_child(child_auth_key, ip)
except ApiException as e:
    print("Exception when calling ResellerApi->associate_ip_to_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **ip** | [**ManageIp**](ManageIp.md)| IP to associate | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_child_domain**
> create_child_domain(child_auth_key, add_child_domain)

Creates a domain for a child account

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
add_child_domain = sib_api_v3_sdk.AddChildDomain() # AddChildDomain | Sender domain to add for a specific child account. This will not be displayed to the parent account.

try:
    # Creates a domain for a child account
    api_instance.create_child_domain(child_auth_key, add_child_domain)
except ApiException as e:
    print("Exception when calling ResellerApi->create_child_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **add_child_domain** | [**AddChildDomain**](AddChildDomain.md)| Sender domain to add for a specific child account. This will not be displayed to the parent account. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reseller_child**
> CreateReseller create_reseller_child(reseller_child=reseller_child)

Creates a reseller child

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
reseller_child = sib_api_v3_sdk.CreateChild() # CreateChild | reseller child to add (optional)

try:
    # Creates a reseller child
    api_response = api_instance.create_reseller_child(reseller_child=reseller_child)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->create_reseller_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reseller_child** | [**CreateChild**](CreateChild.md)| reseller child to add | [optional] 

### Return type

[**CreateReseller**](CreateReseller.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_child_domain**
> delete_child_domain(child_auth_key, domain_name)

Deletes the sender domain of the reseller child based on the childAuthKey and domainName passed

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
domain_name = 'domain_name_example' # str | Pass the existing domain that needs to be deleted

try:
    # Deletes the sender domain of the reseller child based on the childAuthKey and domainName passed
    api_instance.delete_child_domain(child_auth_key, domain_name)
except ApiException as e:
    print("Exception when calling ResellerApi->delete_child_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **domain_name** | **str**| Pass the existing domain that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reseller_child**
> delete_reseller_child(child_auth_key)

Deletes a single reseller child based on the childAuthKey supplied

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child

try:
    # Deletes a single reseller child based on the childAuthKey supplied
    api_instance.delete_reseller_child(child_auth_key)
except ApiException as e:
    print("Exception when calling ResellerApi->delete_reseller_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissociate_ip_from_child**
> dissociate_ip_from_child(child_auth_key, ip)

Dissociate a dedicated IP to the child

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
ip = sib_api_v3_sdk.ManageIp() # ManageIp | IP to dissociate

try:
    # Dissociate a dedicated IP to the child
    api_instance.dissociate_ip_from_child(child_auth_key, ip)
except ApiException as e:
    print("Exception when calling ResellerApi->dissociate_ip_from_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **ip** | [**ManageIp**](ManageIp.md)| IP to dissociate | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_child_account_creation_status**
> GetChildAccountCreationStatus get_child_account_creation_status(child_auth_key)

Returns the status of reseller's child account creation, whether it is successfully created (exists) or not based on the childAuthKey supplied

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child

try:
    # Returns the status of reseller's child account creation, whether it is successfully created (exists) or not based on the childAuthKey supplied
    api_response = api_instance.get_child_account_creation_status(child_auth_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->get_child_account_creation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 

### Return type

[**GetChildAccountCreationStatus**](GetChildAccountCreationStatus.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_child_domains**
> GetChildDomains get_child_domains(child_auth_key)

Gets all the sender domains of a specific child account

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child

try:
    # Gets all the sender domains of a specific child account
    api_response = api_instance.get_child_domains(child_auth_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->get_child_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 

### Return type

[**GetChildDomains**](GetChildDomains.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_child_info**
> GetChildInfo get_child_info(child_auth_key)

Gets the info about a specific child account

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child

try:
    # Gets the info about a specific child account
    api_response = api_instance.get_child_info(child_auth_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->get_child_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 

### Return type

[**GetChildInfo**](GetChildInfo.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reseller_childs**
> GetChildrenList get_reseller_childs(limit=limit, offset=offset)

Gets the list of all reseller's children accounts

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
limit = 10 # int | Number of documents for child accounts information per page (optional) (default to 10)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)

try:
    # Gets the list of all reseller's children accounts
    api_response = api_instance.get_reseller_childs(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->get_reseller_childs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents for child accounts information per page | [optional] [default to 10]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]

### Return type

[**GetChildrenList**](GetChildrenList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_token**
> GetSsoToken get_sso_token(child_auth_key)

Get session token to access Sendinblue (SSO)

It returns a session [token] which will remain valid for a short period of time. A child account will be able to access a white-labeled section by using the following url pattern => https:/email.mydomain.com/login/sso?token=[token]

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child

try:
    # Get session token to access Sendinblue (SSO)
    api_response = api_instance.get_sso_token(child_auth_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->get_sso_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 

### Return type

[**GetSsoToken**](GetSsoToken.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_credits**
> RemainingCreditModel remove_credits(child_auth_key, remove_credits)

Remove Email and/or SMS credits from a specific child account

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
remove_credits = sib_api_v3_sdk.RemoveCredits() # RemoveCredits | Values to post to remove email or SMS credits from a specific child account

try:
    # Remove Email and/or SMS credits from a specific child account
    api_response = api_instance.remove_credits(child_auth_key, remove_credits)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerApi->remove_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **remove_credits** | [**RemoveCredits**](RemoveCredits.md)| Values to post to remove email or SMS credits from a specific child account | 

### Return type

[**RemainingCreditModel**](RemainingCreditModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_child_account_status**
> update_child_account_status(child_auth_key, update_child_account_status)

Updates infos of reseller's child account status based on the childAuthKey supplied

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
update_child_account_status = sib_api_v3_sdk.UpdateChildAccountStatus() # UpdateChildAccountStatus | values to update in child account status

try:
    # Updates infos of reseller's child account status based on the childAuthKey supplied
    api_instance.update_child_account_status(child_auth_key, update_child_account_status)
except ApiException as e:
    print("Exception when calling ResellerApi->update_child_account_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **update_child_account_status** | [**UpdateChildAccountStatus**](UpdateChildAccountStatus.md)| values to update in child account status | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_child_domain**
> update_child_domain(child_auth_key, domain_name, update_child_domain)

Updates the sender domain of reseller's child based on the childAuthKey and domainName passed

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
domain_name = 'domain_name_example' # str | Pass the existing domain that needs to be updated
update_child_domain = sib_api_v3_sdk.UpdateChildDomain() # UpdateChildDomain | value to update for sender domain

try:
    # Updates the sender domain of reseller's child based on the childAuthKey and domainName passed
    api_instance.update_child_domain(child_auth_key, domain_name, update_child_domain)
except ApiException as e:
    print("Exception when calling ResellerApi->update_child_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **domain_name** | **str**| Pass the existing domain that needs to be updated | 
 **update_child_domain** | [**UpdateChildDomain**](UpdateChildDomain.md)| value to update for sender domain | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reseller_child**
> update_reseller_child(child_auth_key, reseller_child)

Updates infos of reseller's child based on the childAuthKey supplied

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
api_instance = sib_api_v3_sdk.ResellerApi(sib_api_v3_sdk.ApiClient(configuration))
child_auth_key = 'child_auth_key_example' # str | auth key of reseller's child
reseller_child = sib_api_v3_sdk.UpdateChild() # UpdateChild | values to update in child profile

try:
    # Updates infos of reseller's child based on the childAuthKey supplied
    api_instance.update_reseller_child(child_auth_key, reseller_child)
except ApiException as e:
    print("Exception when calling ResellerApi->update_reseller_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_auth_key** | **str**| auth key of reseller&#39;s child | 
 **reseller_child** | [**UpdateChild**](UpdateChild.md)| values to update in child profile | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

