# swagger_client.SimApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_annotation_score**](SimApi.md#get_annotation_score) | **GET** /sim/score | Get annotation score
[**get_sim_compare**](SimApi.md#get_sim_compare) | **GET** /sim/compare | Compare a reference profile vs one profiles
[**get_sim_search**](SimApi.md#get_sim_search) | **GET** /sim/search | Search for phenotypically similar diseases or model genes
[**post_annotation_score**](SimApi.md#post_annotation_score) | **POST** /sim/score | Get annotation score
[**post_sim_compare**](SimApi.md#post_sim_compare) | **POST** /sim/compare | Compare a reference profile vs one or more profiles

# **get_annotation_score**
> SufficiencyOutput get_annotation_score(id=id, absent_id=absent_id)

Get annotation score

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimApi()
id = ['id_example'] # list[str] | Phenotype identifier (eg HP:0004935) (optional)
absent_id = ['absent_id_example'] # list[str] | absent phenotype (eg HP:0002828) (optional)

try:
    # Get annotation score
    api_response = api_instance.get_annotation_score(id=id, absent_id=absent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimApi->get_annotation_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| Phenotype identifier (eg HP:0004935) | [optional] 
 **absent_id** | [**list[str]**](str.md)| absent phenotype (eg HP:0002828) | [optional] 

### Return type

[**SufficiencyOutput**](SufficiencyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sim_compare**
> SimResult get_sim_compare(is_feature_set=is_feature_set, metric=metric, ref_id=ref_id, query_id=query_id)

Compare a reference profile vs one profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimApi()
is_feature_set = true # bool | set to true if *all* input ids are phenotypic features, else set to false (optional) (default to true)
metric = 'phenodigm' # str | Metric for computing similarity (optional) (default to phenodigm)
ref_id = ['ref_id_example'] # list[str] | A phenotype or identifier that is composed of phenotypes (eg disease, gene) (optional)
query_id = ['query_id_example'] # list[str] | A phenotype or identifier that is composed of phenotypes (eg disease, gene) (optional)

try:
    # Compare a reference profile vs one profiles
    api_response = api_instance.get_sim_compare(is_feature_set=is_feature_set, metric=metric, ref_id=ref_id, query_id=query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimApi->get_sim_compare: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_feature_set** | **bool**| set to true if *all* input ids are phenotypic features, else set to false | [optional] [default to true]
 **metric** | **str**| Metric for computing similarity | [optional] [default to phenodigm]
 **ref_id** | [**list[str]**](str.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] 
 **query_id** | [**list[str]**](str.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] 

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sim_search**
> SimResult get_sim_search(is_feature_set=is_feature_set, metric=metric, id=id, limit=limit, taxon=taxon)

Search for phenotypically similar diseases or model genes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimApi()
is_feature_set = true # bool | set to true if *all* input ids are phenotypic features, else set to false (optional) (default to true)
metric = 'phenodigm' # str | Metric for computing similarity (optional) (default to phenodigm)
id = ['id_example'] # list[str] | A phenotype or identifier that is composed of phenotypes (eg disease, gene) (optional)
limit = 20 # int | number of rows, max 500 (optional) (default to 20)
taxon = 'taxon_example' # str | ncbi taxon id (optional)

try:
    # Search for phenotypically similar diseases or model genes
    api_response = api_instance.get_sim_search(is_feature_set=is_feature_set, metric=metric, id=id, limit=limit, taxon=taxon)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimApi->get_sim_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_feature_set** | **bool**| set to true if *all* input ids are phenotypic features, else set to false | [optional] [default to true]
 **metric** | **str**| Metric for computing similarity | [optional] [default to phenodigm]
 **id** | [**list[str]**](str.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] 
 **limit** | **int**| number of rows, max 500 | [optional] [default to 20]
 **taxon** | **str**| ncbi taxon id | [optional] 

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_annotation_score**
> SufficiencyOutput post_annotation_score(body)

Get annotation score

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimApi()
body = swagger_client.SufficiencyPostInput() # SufficiencyPostInput | 

try:
    # Get annotation score
    api_response = api_instance.post_annotation_score(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimApi->post_annotation_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SufficiencyPostInput**](SufficiencyPostInput.md)|  | 

### Return type

[**SufficiencyOutput**](SufficiencyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sim_compare**
> SimResult post_sim_compare(body)

Compare a reference profile vs one or more profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimApi()
body = swagger_client.CompareInput() # CompareInput | 

try:
    # Compare a reference profile vs one or more profiles
    api_response = api_instance.post_sim_compare(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimApi->post_sim_compare: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompareInput**](CompareInput.md)|  | 

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

