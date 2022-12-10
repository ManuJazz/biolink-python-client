# swagger_client.MetadataApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata_for_datasets**](MetadataApi.md#get_metadata_for_datasets) | **GET** /metadata/datasets | Get metadata for all datasets from SciGraph

# **get_metadata_for_datasets**
> get_metadata_for_datasets()

Get metadata for all datasets from SciGraph

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Get metadata for all datasets from SciGraph
    api_instance.get_metadata_for_datasets()
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_for_datasets: %s\n" % e)
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

