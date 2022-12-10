# swagger_client.CamApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity_collection**](CamApi.md#get_activity_collection) | **GET** /cam/activity | Returns list of models
[**get_instance_object**](CamApi.md#get_instance_object) | **GET** /cam/instance/{id} | Returns list of matches
[**get_model_collection**](CamApi.md#get_model_collection) | **GET** /cam/model | Returns list of ALL models
[**get_model_contributors**](CamApi.md#get_model_contributors) | **GET** /cam/model/contributors | Returns list of all contributors across all models
[**get_model_instances**](CamApi.md#get_model_instances) | **GET** /cam/instances | Returns list of all instances
[**get_model_object**](CamApi.md#get_model_object) | **GET** /cam/model/{id} | Returns a complete model
[**get_model_properties**](CamApi.md#get_model_properties) | **GET** /cam/model/properties | Returns list of all properties used across all models
[**get_model_property_values**](CamApi.md#get_model_property_values) | **GET** /cam/model/property_values | Returns list property-values for all models
[**get_model_query**](CamApi.md#get_model_query) | **GET** /cam/model/query | Returns list of models matching query
[**get_physical_interaction**](CamApi.md#get_physical_interaction) | **GET** /cam/physical_interaction | Returns list of models

# **get_activity_collection**
> get_activity_collection(title=title, contributor=contributor)

Returns list of models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
title = 'title_example' # str | string to search for in title of model (optional)
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)

try:
    # Returns list of models
    api_instance.get_activity_collection(title=title, contributor=contributor)
except ApiException as e:
    print("Exception when calling CamApi->get_activity_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| string to search for in title of model | [optional] 
 **contributor** | **str**| string to search for in contributor of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_object**
> list[Association] get_instance_object(id, title=title, contributor=contributor)

Returns list of matches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
id = 'id_example' # str | 
title = 'title_example' # str | string to search for in title of model (optional)
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)

try:
    # Returns list of matches
    api_response = api_instance.get_instance_object(id, title=title, contributor=contributor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CamApi->get_instance_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **title** | **str**| string to search for in title of model | [optional] 
 **contributor** | **str**| string to search for in contributor of model | [optional] 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_collection**
> get_model_collection()

Returns list of ALL models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()

try:
    # Returns list of ALL models
    api_instance.get_model_collection()
except ApiException as e:
    print("Exception when calling CamApi->get_model_collection: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_contributors**
> get_model_contributors()

Returns list of all contributors across all models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()

try:
    # Returns list of all contributors across all models
    api_instance.get_model_contributors()
except ApiException as e:
    print("Exception when calling CamApi->get_model_contributors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_instances**
> get_model_instances()

Returns list of all instances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()

try:
    # Returns list of all instances
    api_instance.get_model_instances()
except ApiException as e:
    print("Exception when calling CamApi->get_model_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_object**
> get_model_object(id)

Returns a complete model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
id = 'id_example' # str | 

try:
    # Returns a complete model
    api_instance.get_model_object(id)
except ApiException as e:
    print("Exception when calling CamApi->get_model_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_properties**
> get_model_properties(title=title, contributor=contributor)

Returns list of all properties used across all models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
title = 'title_example' # str | string to search for in title of model (optional)
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)

try:
    # Returns list of all properties used across all models
    api_instance.get_model_properties(title=title, contributor=contributor)
except ApiException as e:
    print("Exception when calling CamApi->get_model_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| string to search for in title of model | [optional] 
 **contributor** | **str**| string to search for in contributor of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_property_values**
> get_model_property_values(title=title, contributor=contributor)

Returns list property-values for all models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
title = 'title_example' # str | string to search for in title of model (optional)
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)

try:
    # Returns list property-values for all models
    api_instance.get_model_property_values(title=title, contributor=contributor)
except ApiException as e:
    print("Exception when calling CamApi->get_model_property_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| string to search for in title of model | [optional] 
 **contributor** | **str**| string to search for in contributor of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_query**
> get_model_query(title=title, contributor=contributor)

Returns list of models matching query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
title = 'title_example' # str | string to search for in title of model (optional)
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)

try:
    # Returns list of models matching query
    api_instance.get_model_query(title=title, contributor=contributor)
except ApiException as e:
    print("Exception when calling CamApi->get_model_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| string to search for in title of model | [optional] 
 **contributor** | **str**| string to search for in contributor of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_physical_interaction**
> get_physical_interaction(title=title, contributor=contributor)

Returns list of models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
title = 'title_example' # str | string to search for in title of model (optional)
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)

try:
    # Returns list of models
    api_instance.get_physical_interaction(title=title, contributor=contributor)
except ApiException as e:
    print("Exception when calling CamApi->get_physical_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| string to search for in title of model | [optional] 
 **contributor** | **str**| string to search for in contributor of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

