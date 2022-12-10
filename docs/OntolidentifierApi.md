# swagger_client.OntolidentifierApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ontol_identifier_resource**](OntolidentifierApi.md#get_ontol_identifier_resource) | **GET** /ontol/identifier/ | Fetches a map from CURIEs/IDs to labels
[**post_ontol_identifier_resource**](OntolidentifierApi.md#post_ontol_identifier_resource) | **POST** /ontol/identifier/ | Fetches a map from CURIEs/IDs to labels

# **get_ontol_identifier_resource**
> get_ontol_identifier_resource(label)

Fetches a map from CURIEs/IDs to labels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolidentifierApi()
label = ['label_example'] # list[str] | List of labels

try:
    # Fetches a map from CURIEs/IDs to labels
    api_instance.get_ontol_identifier_resource(label)
except ApiException as e:
    print("Exception when calling OntolidentifierApi->get_ontol_identifier_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | [**list[str]**](str.md)| List of labels | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ontol_identifier_resource**
> post_ontol_identifier_resource(label)

Fetches a map from CURIEs/IDs to labels

Takes 'label' list argument either as a querystring argument or as a key in the POST body when content-type is application/json.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolidentifierApi()
label = ['label_example'] # list[str] | List of labels

try:
    # Fetches a map from CURIEs/IDs to labels
    api_instance.post_ontol_identifier_resource(label)
except ApiException as e:
    print("Exception when calling OntolidentifierApi->post_ontol_identifier_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | [**list[str]**](str.md)| List of labels | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

