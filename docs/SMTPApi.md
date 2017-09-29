# sib_api_v3_sdk.SMTPApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_smtp_template**](SMTPApi.md#create_smtp_template) | **POST** /smtp/templates | Create an smtp template
[**delete_hardbounces**](SMTPApi.md#delete_hardbounces) | **POST** /smtp/deleteHardbounces | Delete hardbounces
[**get_aggregated_smtp_report**](SMTPApi.md#get_aggregated_smtp_report) | **GET** /smtp/statistics/aggregatedReport | Get your SMTP activity aggregated over a period of time
[**get_email_event_report**](SMTPApi.md#get_email_event_report) | **GET** /smtp/statistics/events | Get all your SMTP activity (unaggregated events)
[**get_smtp_report**](SMTPApi.md#get_smtp_report) | **GET** /smtp/statistics/reports | Get your SMTP activity aggregated per day
[**get_smtp_template**](SMTPApi.md#get_smtp_template) | **GET** /smtp/templates/{templateId} | Returns the template informations
[**get_smtp_templates**](SMTPApi.md#get_smtp_templates) | **GET** /smtp/templates | Get the list of SMTP templates
[**send_template**](SMTPApi.md#send_template) | **POST** /smtp/templates/{templateId}/send | Send a template
[**send_test_template**](SMTPApi.md#send_test_template) | **POST** /smtp/templates/{templateId}/sendTest | Send a template to your test list
[**send_transac_email**](SMTPApi.md#send_transac_email) | **POST** /smtp/email | Send a transactional email
[**update_smtp_template**](SMTPApi.md#update_smtp_template) | **PUT** /smtp/templates/{templateId} | Updates an smtp templates


# **create_smtp_template**
> CreateModel create_smtp_template(smtp_template)

Create an smtp template

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
api_instance = sib_api_v3_sdk.SMTPApi()
smtp_template = sib_api_v3_sdk.CreateSmtpTemplate() # CreateSmtpTemplate | values to update in smtp template

try: 
    # Create an smtp template
    api_response = api_instance.create_smtp_template(smtp_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->create_smtp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_template** | [**CreateSmtpTemplate**](CreateSmtpTemplate.md)| values to update in smtp template | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hardbounces**
> delete_hardbounces(delete_hardbounces=delete_hardbounces)

Delete hardbounces

Delete hardbounces. To use carefully (e.g. in case of temporary ISP failures)

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
api_instance = sib_api_v3_sdk.SMTPApi()
delete_hardbounces = sib_api_v3_sdk.DeleteHardbounces() # DeleteHardbounces | values to delete hardbounces (optional)

try: 
    # Delete hardbounces
    api_instance.delete_hardbounces(delete_hardbounces=delete_hardbounces)
except ApiException as e:
    print("Exception when calling SMTPApi->delete_hardbounces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_hardbounces** | [**DeleteHardbounces**](DeleteHardbounces.md)| values to delete hardbounces | [optional] 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_smtp_report**
> GetAggregatedReport get_aggregated_smtp_report(start_date=start_date, end_date=end_date, days=days, tag=tag)

Get your SMTP activity aggregated over a period of time

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
api_instance = sib_api_v3_sdk.SMTPApi()
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate (optional)
days = 56 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
tag = 'tag_example' # str | Tag of the emails (optional)

try: 
    # Get your SMTP activity aggregated over a period of time
    api_response = api_instance.get_aggregated_smtp_report(start_date=start_date, end_date=end_date, days=days, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->get_aggregated_smtp_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **tag** | **str**| Tag of the emails | [optional] 

### Return type

[**GetAggregatedReport**](GetAggregatedReport.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_event_report**
> GetEmailEventReport get_email_event_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, email=email, event=event, tags=tags, message_id=message_id, template_id=template_id)

Get all your SMTP activity (unaggregated events)

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
api_instance = sib_api_v3_sdk.SMTPApi()
limit = 50 # int | Number limitation for the result returned (optional) (default to 50)
offset = 0 # int | Beginning point in the list to retrieve from. (optional) (default to 0)
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate (optional)
days = 56 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
email = 'email_example' # str | Filter the report for a specific email addresses (optional)
event = 'event_example' # str | Filter the report for a specific event type (optional)
tags = 'tags_example' # str | Filter the report for tags (serialized and urlencoded array) (optional)
message_id = 'message_id_example' # str | Filter on a specific message id (optional)
template_id = 789 # int | Filter on a specific template id (optional)

try: 
    # Get all your SMTP activity (unaggregated events)
    api_response = api_instance.get_email_event_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, email=email, event=event, tags=tags, message_id=message_id, template_id=template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->get_email_event_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number limitation for the result returned | [optional] [default to 50]
 **offset** | **int**| Beginning point in the list to retrieve from. | [optional] [default to 0]
 **start_date** | **date**| Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **email** | **str**| Filter the report for a specific email addresses | [optional] 
 **event** | **str**| Filter the report for a specific event type | [optional] 
 **tags** | **str**| Filter the report for tags (serialized and urlencoded array) | [optional] 
 **message_id** | **str**| Filter on a specific message id | [optional] 
 **template_id** | **int**| Filter on a specific template id | [optional] 

### Return type

[**GetEmailEventReport**](GetEmailEventReport.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_report**
> GetReports get_smtp_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, tag=tag)

Get your SMTP activity aggregated per day

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
api_instance = sib_api_v3_sdk.SMTPApi()
limit = 50 # int | Number of documents returned per page (optional) (default to 50)
offset = 0 # int | Index of the first document on the page (optional) (default to 0)
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD) (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD) (optional)
days = 56 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
tag = 'tag_example' # str | Tag of the emails (optional)

try: 
    # Get your SMTP activity aggregated per day
    api_response = api_instance.get_smtp_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->get_smtp_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents returned per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document on the page | [optional] [default to 0]
 **start_date** | **date**| Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD) | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD) | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **tag** | **str**| Tag of the emails | [optional] 

### Return type

[**GetReports**](GetReports.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_template**
> GetSmtpTemplateOverview get_smtp_template(template_id)

Returns the template informations

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
api_instance = sib_api_v3_sdk.SMTPApi()
template_id = 789 # int | id of the template

try: 
    # Returns the template informations
    api_response = api_instance.get_smtp_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->get_smtp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| id of the template | 

### Return type

[**GetSmtpTemplateOverview**](GetSmtpTemplateOverview.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_templates**
> GetSmtpTemplates get_smtp_templates(template_status=template_status, limit=limit, offset=offset)

Get the list of SMTP templates

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
api_instance = sib_api_v3_sdk.SMTPApi()
template_status = true # bool | Filter on the status of the template. Active = true, inactive = false (optional)
limit = 50 # int | Number of documents returned per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)

try: 
    # Get the list of SMTP templates
    api_response = api_instance.get_smtp_templates(template_status=template_status, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->get_smtp_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_status** | **bool**| Filter on the status of the template. Active &#x3D; true, inactive &#x3D; false | [optional] 
 **limit** | **int**| Number of documents returned per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]

### Return type

[**GetSmtpTemplates**](GetSmtpTemplates.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_template**
> SendTemplateEmail send_template(template_id, send_email)

Send a template

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
api_instance = sib_api_v3_sdk.SMTPApi()
template_id = 789 # int | Id of the template
send_email = sib_api_v3_sdk.SendEmail() # SendEmail | 

try: 
    # Send a template
    api_response = api_instance.send_template(template_id, send_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Id of the template | 
 **send_email** | [**SendEmail**](SendEmail.md)|  | 

### Return type

[**SendTemplateEmail**](SendTemplateEmail.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_template**
> send_test_template(template_id, send_test_email)

Send a template to your test list

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
api_instance = sib_api_v3_sdk.SMTPApi()
template_id = 789 # int | Id of the template
send_test_email = sib_api_v3_sdk.SendTestEmail() # SendTestEmail | 

try: 
    # Send a template to your test list
    api_instance.send_test_template(template_id, send_test_email)
except ApiException as e:
    print("Exception when calling SMTPApi->send_test_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Id of the template | 
 **send_test_email** | [**SendTestEmail**](SendTestEmail.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_transac_email**
> CreateSmtpEmail send_transac_email(send_smtp_email)

Send a transactional email

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
api_instance = sib_api_v3_sdk.SMTPApi()
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail() # SendSmtpEmail | Values to send a transactional email

try: 
    # Send a transactional email
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_smtp_email** | [**SendSmtpEmail**](SendSmtpEmail.md)| Values to send a transactional email | 

### Return type

[**CreateSmtpEmail**](CreateSmtpEmail.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smtp_template**
> update_smtp_template(template_id, smtp_template)

Updates an smtp templates

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
api_instance = sib_api_v3_sdk.SMTPApi()
template_id = 789 # int | id of the template
smtp_template = sib_api_v3_sdk.UpdateSmtpTemplate() # UpdateSmtpTemplate | values to update in smtp template

try: 
    # Updates an smtp templates
    api_instance.update_smtp_template(template_id, smtp_template)
except ApiException as e:
    print("Exception when calling SMTPApi->update_smtp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| id of the template | 
 **smtp_template** | [**UpdateSmtpTemplate**](UpdateSmtpTemplate.md)| values to update in smtp template | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

