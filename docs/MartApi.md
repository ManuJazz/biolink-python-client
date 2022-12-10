# swagger_client.MartApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mart_case_associations_resource**](MartApi.md#get_mart_case_associations_resource) | **GET** /mart/case/{object_category}/{taxon} | Bulk download of case associations
[**get_mart_disease_associations_resource**](MartApi.md#get_mart_disease_associations_resource) | **GET** /mart/disease/{object_category}/{taxon} | Bulk download of disease associations
[**get_mart_gene_associations_resource**](MartApi.md#get_mart_gene_associations_resource) | **GET** /mart/gene/{object_category}/{taxon} | Bulk download of gene associations
[**get_mart_ortholog_associations_resource**](MartApi.md#get_mart_ortholog_associations_resource) | **GET** /mart/ortholog/{taxon1}/{taxon2} | Bulk download of orthologs
[**get_mart_paralog_associations_resource**](MartApi.md#get_mart_paralog_associations_resource) | **GET** /mart/paralog/{taxon1}/{taxon2} | Bulk download of paralogs

# **get_mart_case_associations_resource**
> get_mart_case_associations_resource(taxon, object_category, slim=slim)

Bulk download of case associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
taxon = 'taxon_example' # str | taxon of case, must be of form NCBITaxon:9606
object_category = 'object_category_example' # str | Category of entity at link Subject (target), e.g. phenotype, disease
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try:
    # Bulk download of case associations
    api_instance.get_mart_case_associations_resource(taxon, object_category, slim=slim)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_case_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| taxon of case, must be of form NCBITaxon:9606 | 
 **object_category** | **str**| Category of entity at link Subject (target), e.g. phenotype, disease | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mart_disease_associations_resource**
> get_mart_disease_associations_resource(taxon, object_category, slim=slim)

Bulk download of disease associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
taxon = 'taxon_example' # str | taxon of disease, must be of form NCBITaxon:9606
object_category = 'object_category_example' # str | Category of entity at link Object (target), e.g. phenotype, disease
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try:
    # Bulk download of disease associations
    api_instance.get_mart_disease_associations_resource(taxon, object_category, slim=slim)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_disease_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| taxon of disease, must be of form NCBITaxon:9606 | 
 **object_category** | **str**| Category of entity at link Object (target), e.g. phenotype, disease | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mart_gene_associations_resource**
> get_mart_gene_associations_resource(taxon, object_category, slim=slim)

Bulk download of gene associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
taxon = 'taxon_example' # str | taxon of gene, must be of form NCBITaxon:9606
object_category = 'object_category_example' # str | Category of entity at link Object (target), e.g. phenotype, disease
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try:
    # Bulk download of gene associations
    api_instance.get_mart_gene_associations_resource(taxon, object_category, slim=slim)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_gene_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| taxon of gene, must be of form NCBITaxon:9606 | 
 **object_category** | **str**| Category of entity at link Object (target), e.g. phenotype, disease | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mart_ortholog_associations_resource**
> get_mart_ortholog_associations_resource(taxon2, taxon1)

Bulk download of orthologs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
taxon2 = 'taxon2_example' # str | object taxon, e.g. NCBITaxon:10090
taxon1 = 'taxon1_example' # str | subject taxon, e.g. NCBITaxon:9606

try:
    # Bulk download of orthologs
    api_instance.get_mart_ortholog_associations_resource(taxon2, taxon1)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_ortholog_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon2** | **str**| object taxon, e.g. NCBITaxon:10090 | 
 **taxon1** | **str**| subject taxon, e.g. NCBITaxon:9606 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mart_paralog_associations_resource**
> get_mart_paralog_associations_resource(taxon2, taxon1)

Bulk download of paralogs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
taxon2 = 'taxon2_example' # str | object taxon, e.g. NCBITaxon:9606
taxon1 = 'taxon1_example' # str | subject taxon, e.g. NCBITaxon:9606

try:
    # Bulk download of paralogs
    api_instance.get_mart_paralog_associations_resource(taxon2, taxon1)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_paralog_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon2** | **str**| object taxon, e.g. NCBITaxon:9606 | 
 **taxon1** | **str**| subject taxon, e.g. NCBITaxon:9606 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

