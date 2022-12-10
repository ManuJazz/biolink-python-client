# swagger_client.RelationusageApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_relation_usage_between_resource**](RelationusageApi.md#get_relation_usage_between_resource) | **GET** /relation/usage/between/{subject_category}/{object_category} | All relations used plus count of associations
[**get_relation_usage_pivot_label_resource**](RelationusageApi.md#get_relation_usage_pivot_label_resource) | **GET** /relation/usage/pivot/label | Relation usage count for all subj x obj category combinations, showing label
[**get_relation_usage_pivot_resource**](RelationusageApi.md#get_relation_usage_pivot_resource) | **GET** /relation/usage/pivot | Relation usage count for all subj x obj category combinations
[**get_relation_usage_resource**](RelationusageApi.md#get_relation_usage_resource) | **GET** /relation/usage/ | All relations used plus count of associations

# **get_relation_usage_between_resource**
> list[AssociationResults] get_relation_usage_between_resource(subject_category, object_category, subject_taxon=subject_taxon, evidence=evidence)

All relations used plus count of associations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationusageApi()
subject_category = 'subject_category_example' # str | 
object_category = 'object_category_example' # str | 
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)

try:
    # All relations used plus count of associations
    api_response = api_instance.get_relation_usage_between_resource(subject_category, object_category, subject_taxon=subject_taxon, evidence=evidence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationusageApi->get_relation_usage_between_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_category** | **str**|  | 
 **object_category** | **str**|  | 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_usage_pivot_label_resource**
> list[AssociationResults] get_relation_usage_pivot_label_resource(subject_taxon=subject_taxon, evidence=evidence)

Relation usage count for all subj x obj category combinations, showing label

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationusageApi()
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)

try:
    # Relation usage count for all subj x obj category combinations, showing label
    api_response = api_instance.get_relation_usage_pivot_label_resource(subject_taxon=subject_taxon, evidence=evidence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationusageApi->get_relation_usage_pivot_label_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_usage_pivot_resource**
> list[AssociationResults] get_relation_usage_pivot_resource(subject_taxon=subject_taxon, evidence=evidence)

Relation usage count for all subj x obj category combinations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationusageApi()
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)

try:
    # Relation usage count for all subj x obj category combinations
    api_response = api_instance.get_relation_usage_pivot_resource(subject_taxon=subject_taxon, evidence=evidence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationusageApi->get_relation_usage_pivot_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_usage_resource**
> list[AssociationResults] get_relation_usage_resource(subject_taxon=subject_taxon, evidence=evidence)

All relations used plus count of associations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationusageApi()
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)

try:
    # All relations used plus count of associations
    api_response = api_instance.get_relation_usage_resource(subject_taxon=subject_taxon, evidence=evidence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationusageApi->get_relation_usage_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

