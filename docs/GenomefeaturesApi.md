# swagger_client.GenomefeaturesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_features_within_resource**](GenomefeaturesApi.md#get_features_within_resource) | **GET** /genome/features/within/{build}/{reference}/{begin}/{end} | Returns list of matches

# **get_features_within_resource**
> list[SequenceFeature] get_features_within_resource(build, reference, begin, end)

Returns list of matches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenomefeaturesApi()
build = 'build_example' # str | 
reference = 'reference_example' # str | 
begin = 'begin_example' # str | 
end = 'end_example' # str | 

try:
    # Returns list of matches
    api_response = api_instance.get_features_within_resource(build, reference, begin, end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenomefeaturesApi->get_features_within_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build** | **str**|  | 
 **reference** | **str**|  | 
 **begin** | **str**|  | 
 **end** | **str**|  | 

### Return type

[**list[SequenceFeature]**](SequenceFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

