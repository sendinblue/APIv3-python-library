# sib_api_v3_sdk.EcommerceApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_order**](EcommerceApi.md#create_batch_order) | **POST** /orders/status/batch | Create orders in batch
[**create_order**](EcommerceApi.md#create_order) | **POST** /orders/status | Managing the status of the order
[**create_update_batch_category**](EcommerceApi.md#create_update_batch_category) | **POST** /categories/batch | Create categories in batch
[**create_update_batch_products**](EcommerceApi.md#create_update_batch_products) | **POST** /products/batch | Create products in batch
[**create_update_category**](EcommerceApi.md#create_update_category) | **POST** /categories | Create/Update a category
[**create_update_product**](EcommerceApi.md#create_update_product) | **POST** /products | Create/Update a product
[**ecommerce_activate_post**](EcommerceApi.md#ecommerce_activate_post) | **POST** /ecommerce/activate | Activate the eCommerce app
[**get_categories**](EcommerceApi.md#get_categories) | **GET** /categories | Return all your categories
[**get_category_info**](EcommerceApi.md#get_category_info) | **GET** /categories/{id} | Get a category details
[**get_product_info**](EcommerceApi.md#get_product_info) | **GET** /products/{id} | Get a product&#39;s details
[**get_products**](EcommerceApi.md#get_products) | **GET** /products | Return all your products


# **create_batch_order**
> create_batch_order(order_batch)

Create orders in batch

Create multiple orders at one time instead of one order at a time

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
order_batch = sib_api_v3_sdk.OrderBatch() # OrderBatch | 

try:
    # Create orders in batch
    api_instance.create_batch_order(order_batch)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_batch_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_batch** | [**OrderBatch**](OrderBatch.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> create_order(order)

Managing the status of the order

Manages the transactional status of the order

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
order = sib_api_v3_sdk.Order() # Order | 

try:
    # Managing the status of the order
    api_instance.create_order(order)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_batch_category**
> CreateUpdateBatchCategoryModel create_update_batch_category(create_update_batch_category)

Create categories in batch

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
create_update_batch_category = sib_api_v3_sdk.CreateUpdateBatchCategory() # CreateUpdateBatchCategory | Values to create a batch of categories

try:
    # Create categories in batch
    api_response = api_instance.create_update_batch_category(create_update_batch_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_batch_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_batch_category** | [**CreateUpdateBatchCategory**](CreateUpdateBatchCategory.md)| Values to create a batch of categories | 

### Return type

[**CreateUpdateBatchCategoryModel**](CreateUpdateBatchCategoryModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_batch_products**
> CreateUpdateBatchProductsModel create_update_batch_products(create_update_batch_products)

Create products in batch

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
create_update_batch_products = sib_api_v3_sdk.CreateUpdateBatchProducts() # CreateUpdateBatchProducts | Values to create a batch of products

try:
    # Create products in batch
    api_response = api_instance.create_update_batch_products(create_update_batch_products)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_batch_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_batch_products** | [**CreateUpdateBatchProducts**](CreateUpdateBatchProducts.md)| Values to create a batch of products | 

### Return type

[**CreateUpdateBatchProductsModel**](CreateUpdateBatchProductsModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_category**
> CreateCategoryModel create_update_category(create_update_category)

Create/Update a category

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
create_update_category = sib_api_v3_sdk.CreateUpdateCategory() # CreateUpdateCategory | Values to create/update a category

try:
    # Create/Update a category
    api_response = api_instance.create_update_category(create_update_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_category** | [**CreateUpdateCategory**](CreateUpdateCategory.md)| Values to create/update a category | 

### Return type

[**CreateCategoryModel**](CreateCategoryModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_product**
> CreateProductModel create_update_product(create_update_product)

Create/Update a product

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
create_update_product = sib_api_v3_sdk.CreateUpdateProduct() # CreateUpdateProduct | Values to create/update a product

try:
    # Create/Update a product
    api_response = api_instance.create_update_product(create_update_product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_product** | [**CreateUpdateProduct**](CreateUpdateProduct.md)| Values to create/update a product | 

### Return type

[**CreateProductModel**](CreateProductModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ecommerce_activate_post**
> ecommerce_activate_post()

Activate the eCommerce app

Getting access to Sendinblue eCommerce.

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))

try:
    # Activate the eCommerce app
    api_instance.ecommerce_activate_post()
except ApiException as e:
    print("Exception when calling EcommerceApi->ecommerce_activate_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> GetCategories get_categories(limit=limit, offset=offset, sort=sort, ids=ids, name=name)

Return all your categories

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)
ids = ['ids_example'] # list[str] | Filter by category ids (optional)
name = 'name_example' # str | Filter by category name (optional)

try:
    # Return all your categories
    api_response = api_instance.get_categories(limit=limit, offset=offset, sort=sort, ids=ids, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **ids** | [**list[str]**](str.md)| Filter by category ids | [optional] 
 **name** | **str**| Filter by category name | [optional] 

### Return type

[**GetCategories**](GetCategories.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_info**
> GetCategoryDetails get_category_info(id)

Get a category details

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | Category ID

try:
    # Get a category details
    api_response = api_instance.get_category_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_category_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Category ID | 

### Return type

[**GetCategoryDetails**](GetCategoryDetails.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_info**
> GetProductDetails get_product_info(id)

Get a product's details

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
id = 'id_example' # str | Product ID

try:
    # Get a product's details
    api_response = api_instance.get_product_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_product_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Product ID | 

### Return type

[**GetProductDetails**](GetProductDetails.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> GetProducts get_products(limit=limit, offset=offset, sort=sort, ids=ids, name=name, price=price, categories=categories)

Return all your products

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
api_instance = sib_api_v3_sdk.EcommerceApi(sib_api_v3_sdk.ApiClient(configuration))
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)
ids = ['ids_example'] # list[str] | Filter by product ids (optional)
name = 'name_example' # str | Filter by product name, minimum 3 characters should be present for search (optional)
price = ['price_example'] # list[str] | Filter by product price, like price[lte] (optional)
categories = ['categories_example'] # list[str] | Filter by category ids (optional)

try:
    # Return all your products
    api_response = api_instance.get_products(limit=limit, offset=offset, sort=sort, ids=ids, name=name, price=price, categories=categories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **ids** | [**list[str]**](str.md)| Filter by product ids | [optional] 
 **name** | **str**| Filter by product name, minimum 3 characters should be present for search | [optional] 
 **price** | [**list[str]**](str.md)| Filter by product price, like price[lte] | [optional] 
 **categories** | [**list[str]**](str.md)| Filter by category ids | [optional] 

### Return type

[**GetProducts**](GetProducts.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

