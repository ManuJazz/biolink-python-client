# swagger_client.BioentitysethomologsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_set_homologs**](BioentitysethomologsApi.md#get_entity_set_homologs) | **GET** /bioentityset/homologs/ | Returns homology associations for a given input set of genes

# **get_entity_set_homologs**
> list[AssociationResults] get_entity_set_homologs(subject=subject)

Returns homology associations for a given input set of genes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysethomologsApi()
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)

try:
    # Returns homology associations for a given input set of genes
    api_response = api_instance.get_entity_set_homologs(subject=subject)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentitysethomologsApi->get_entity_set_homologs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

