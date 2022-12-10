# swagger_client.PairsimApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pair_sim_jaccard_resource**](PairsimApi.md#get_pair_sim_jaccard_resource) | **GET** /pair/sim/jaccard/{id1}/{id2} | Get pairwise similarity

# **get_pair_sim_jaccard_resource**
> get_pair_sim_jaccard_resource(id2, id1, object_category=object_category)

Get pairwise similarity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PairsimApi()
id2 = 'id2_example' # str | id, e.g. NCBIGene:1200; ZFIN:ZDB-GENE-980528-2059; UniProtKB:P12644
id1 = 'id1_example' # str | id, e.g. NCBIGene:10891; ZFIN:ZDB-GENE-980526-166; UniProtKB:Q15465
object_category = 'object_category_example' # str | e.g. disease, phenotype, gene. Two subjects will be compared based on overlap between associations to objects in this category (optional)

try:
    # Get pairwise similarity
    api_instance.get_pair_sim_jaccard_resource(id2, id1, object_category=object_category)
except ApiException as e:
    print("Exception when calling PairsimApi->get_pair_sim_jaccard_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id2** | **str**| id, e.g. NCBIGene:1200; ZFIN:ZDB-GENE-980528-2059; UniProtKB:P12644 | 
 **id1** | **str**| id, e.g. NCBIGene:10891; ZFIN:ZDB-GENE-980526-166; UniProtKB:Q15465 | 
 **object_category** | **str**| e.g. disease, phenotype, gene. Two subjects will be compared based on overlap between associations to objects in this category | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

