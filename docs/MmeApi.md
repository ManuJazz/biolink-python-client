# swagger_client.MmeApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_disease_mme**](MmeApi.md#post_disease_mme) | **POST** /mme/disease | Match a patient to diseases based on their phenotypes
[**post_fly_mme**](MmeApi.md#post_fly_mme) | **POST** /mme/fly | Match a patient to fruit fly genes based on similar phenotypes
[**post_mouse_mme**](MmeApi.md#post_mouse_mme) | **POST** /mme/mouse | Match a patient to mouse genes based on similar phenotypes
[**post_nematode_mme**](MmeApi.md#post_nematode_mme) | **POST** /mme/nematode | Match a patient to nematode genes based on similar phenotypes
[**post_zebrafish_mme**](MmeApi.md#post_zebrafish_mme) | **POST** /mme/zebrafish | Match a patient to zebrafish genes based on similar phenotypes

# **post_disease_mme**
> post_disease_mme(body)

Match a patient to diseases based on their phenotypes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MmeApi()
body = swagger_client.Mme() # Mme | 

try:
    # Match a patient to diseases based on their phenotypes
    api_instance.post_disease_mme(body)
except ApiException as e:
    print("Exception when calling MmeApi->post_disease_mme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Mme**](Mme.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fly_mme**
> post_fly_mme(body)

Match a patient to fruit fly genes based on similar phenotypes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MmeApi()
body = swagger_client.Mme() # Mme | 

try:
    # Match a patient to fruit fly genes based on similar phenotypes
    api_instance.post_fly_mme(body)
except ApiException as e:
    print("Exception when calling MmeApi->post_fly_mme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Mme**](Mme.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mouse_mme**
> post_mouse_mme(body)

Match a patient to mouse genes based on similar phenotypes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MmeApi()
body = swagger_client.Mme() # Mme | 

try:
    # Match a patient to mouse genes based on similar phenotypes
    api_instance.post_mouse_mme(body)
except ApiException as e:
    print("Exception when calling MmeApi->post_mouse_mme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Mme**](Mme.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nematode_mme**
> post_nematode_mme(body)

Match a patient to nematode genes based on similar phenotypes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MmeApi()
body = swagger_client.Mme() # Mme | 

try:
    # Match a patient to nematode genes based on similar phenotypes
    api_instance.post_nematode_mme(body)
except ApiException as e:
    print("Exception when calling MmeApi->post_nematode_mme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Mme**](Mme.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_zebrafish_mme**
> post_zebrafish_mme(body)

Match a patient to zebrafish genes based on similar phenotypes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MmeApi()
body = swagger_client.Mme() # Mme | 

try:
    # Match a patient to zebrafish genes based on similar phenotypes
    api_instance.post_zebrafish_mme(body)
except ApiException as e:
    print("Exception when calling MmeApi->post_zebrafish_mme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Mme**](Mme.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

