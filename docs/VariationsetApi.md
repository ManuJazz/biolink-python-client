# swagger_client.VariationsetApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_variant_set_item**](VariationsetApi.md#delete_variant_set_item) | **DELETE** /variation/set/{id} | Deletes variant set
[**get_variant_analyze**](VariationsetApi.md#get_variant_analyze) | **GET** /variation/set/analyze/{id} | Returns list of matches
[**get_variant_set_item**](VariationsetApi.md#get_variant_set_item) | **GET** /variation/set/{id} | Returns a variant set
[**get_variant_sets_archive_collection**](VariationsetApi.md#get_variant_sets_archive_collection) | **GET** /variation/set/archive/{year}/{month}/{day} | Returns list of variant sets from a specified time period
[**get_variant_sets_collection**](VariationsetApi.md#get_variant_sets_collection) | **GET** /variation/set/ | Returns list of variant sets
[**post_variant_sets_collection**](VariationsetApi.md#post_variant_sets_collection) | **POST** /variation/set/ | Creates a new variant set
[**put_variant_set_item**](VariationsetApi.md#put_variant_set_item) | **PUT** /variation/set/{id} | Updates a variant set

# **delete_variant_set_item**
> delete_variant_set_item(id)

Deletes variant set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariationsetApi()
id = 'id_example' # str | 

try:
    # Deletes variant set
    api_instance.delete_variant_set_item(id)
except ApiException as e:
    print("Exception when calling VariationsetApi->delete_variant_set_item: %s\n" % e)
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

# **get_variant_analyze**
> list[Association] get_variant_analyze(id)

Returns list of matches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariationsetApi()
id = 'id_example' # str | 

try:
    # Returns list of matches
    api_response = api_instance.get_variant_analyze(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariationsetApi->get_variant_analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_set_item**
> VariantSet get_variant_set_item(id)

Returns a variant set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariationsetApi()
id = 'id_example' # str | 

try:
    # Returns a variant set
    api_response = api_instance.get_variant_set_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariationsetApi->get_variant_set_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VariantSet**](VariantSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_sets_archive_collection**
> PageOfVariantSets get_variant_sets_archive_collection(year, month, day, page=page, per_page=per_page)

Returns list of variant sets from a specified time period

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariationsetApi()
year = 56 # int | 
month = 56 # int | 
day = 56 # int | 
page = 1 # int | Page number (optional) (default to 1)
per_page = 10 # int | Results per page {error_msg} (optional) (default to 10)

try:
    # Returns list of variant sets from a specified time period
    api_response = api_instance.get_variant_sets_archive_collection(year, month, day, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariationsetApi->get_variant_sets_archive_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **month** | **int**|  | 
 **day** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Results per page {error_msg} | [optional] [default to 10]

### Return type

[**PageOfVariantSets**](PageOfVariantSets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_sets_collection**
> PageOfVariantSets get_variant_sets_collection(page=page, per_page=per_page)

Returns list of variant sets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariationsetApi()
page = 1 # int | Page number (optional) (default to 1)
per_page = 10 # int | Results per page {error_msg} (optional) (default to 10)

try:
    # Returns list of variant sets
    api_response = api_instance.get_variant_sets_collection(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariationsetApi->get_variant_sets_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Results per page {error_msg} | [optional] [default to 10]

### Return type

[**PageOfVariantSets**](PageOfVariantSets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_variant_sets_collection**
> post_variant_sets_collection(body)

Creates a new variant set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariationsetApi()
body = swagger_client.VariantSet() # VariantSet | 

try:
    # Creates a new variant set
    api_instance.post_variant_sets_collection(body)
except ApiException as e:
    print("Exception when calling VariationsetApi->post_variant_sets_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariantSet**](VariantSet.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_variant_set_item**
> put_variant_set_item(body, id)

Updates a variant set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariationsetApi()
body = swagger_client.VariantSet() # VariantSet | 
id = 'id_example' # str | 

try:
    # Updates a variant set
    api_instance.put_variant_set_item(body, id)
except ApiException as e:
    print("Exception when calling VariationsetApi->put_variant_set_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariantSet**](VariantSet.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

