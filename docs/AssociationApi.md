# swagger_client.AssociationApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_association_by_subject_and_assoc_type**](AssociationApi.md#get_association_by_subject_and_assoc_type) | **GET** /association/type/{association_type} | Returns list of matching associations of a given type
[**get_association_by_subject_and_object_category_search**](AssociationApi.md#get_association_by_subject_and_object_category_search) | **GET** /association/find/{subject_category}/{object_category} | Returns list of matching associations between a given subject and object category
[**get_association_by_subject_category_search**](AssociationApi.md#get_association_by_subject_category_search) | **GET** /association/find/{subject_category} | Returns list of matching associations for a given subject category
[**get_association_object**](AssociationApi.md#get_association_object) | **GET** /association/{id} | Returns the association with a given identifier
[**get_associations_between**](AssociationApi.md#get_associations_between) | **GET** /association/between/{subject}/{object} | Returns associations connecting two entities
[**get_associations_from**](AssociationApi.md#get_associations_from) | **GET** /association/from/{subject} | Returns list of matching associations starting from a given subject (source)
[**get_associations_to**](AssociationApi.md#get_associations_to) | **GET** /association/to/{object} | Returns list of matching associations pointing to a given object (target)

# **get_association_by_subject_and_assoc_type**
> list[AssociationResults] get_association_by_subject_and_assoc_type(association_type, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, subject=subject, object=object)

Returns list of matching associations of a given type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
association_type = 'association_type_example' # str | Association type, eg gene_phenotype
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
subject = 'subject_example' # str | Subject CURIE (optional)
object = 'object_example' # str | Object CURIE (optional)

try:
    # Returns list of matching associations of a given type
    api_response = api_instance.get_association_by_subject_and_assoc_type(association_type, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, subject=subject, object=object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_by_subject_and_assoc_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_type** | **str**| Association type, eg gene_phenotype | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **subject** | **str**| Subject CURIE | [optional] 
 **object** | **str**| Object CURIE | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_by_subject_and_object_category_search**
> list[AssociationResults] get_association_by_subject_and_object_category_search(object_category, subject_category, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, subject=subject, object=object, subject_taxon=subject_taxon, object_taxon=object_taxon, relation=relation)

Returns list of matching associations between a given subject and object category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
object_category = 'object_category_example' # str | Category of entity at link Object (target), e.g. gene, disease, phenotype
subject_category = 'subject_category_example' # str | Category of entity at link Subject (source), e.g. gene, disease, phenotype
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
subject = 'subject_example' # str | Subject CURIE (optional)
object = 'object_example' # str | Object CURIE (optional)
subject_taxon = 'subject_taxon_example' # str | Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) (optional)
object_taxon = 'object_taxon_example' # str | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) (optional)
relation = 'relation_example' # str | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. (optional)

try:
    # Returns list of matching associations between a given subject and object category
    api_response = api_instance.get_association_by_subject_and_object_category_search(object_category, subject_category, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, subject=subject, object=object, subject_taxon=subject_taxon, object_taxon=object_taxon, relation=relation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_by_subject_and_object_category_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_category** | **str**| Category of entity at link Object (target), e.g. gene, disease, phenotype | 
 **subject_category** | **str**| Category of entity at link Subject (source), e.g. gene, disease, phenotype | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **subject** | **str**| Subject CURIE | [optional] 
 **object** | **str**| Object CURIE | [optional] 
 **subject_taxon** | **str**| Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) | [optional] 
 **object_taxon** | **str**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] 
 **relation** | **str**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_by_subject_category_search**
> list[AssociationResults] get_association_by_subject_category_search(subject_category, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, subject_taxon=subject_taxon, object_taxon=object_taxon, relation=relation)

Returns list of matching associations for a given subject category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
subject_category = 'subject_category_example' # str | Category of entity at link Subject (source), e.g. gene, disease, phenotype
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
subject_taxon = 'subject_taxon_example' # str | Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) (optional)
object_taxon = 'object_taxon_example' # str | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) (optional)
relation = 'relation_example' # str | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. (optional)

try:
    # Returns list of matching associations for a given subject category
    api_response = api_instance.get_association_by_subject_category_search(subject_category, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, subject_taxon=subject_taxon, object_taxon=object_taxon, relation=relation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_by_subject_category_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_category** | **str**| Category of entity at link Subject (source), e.g. gene, disease, phenotype | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **subject_taxon** | **str**| Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) | [optional] 
 **object_taxon** | **str**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] 
 **relation** | **str**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_object**
> list[AssociationResults] get_association_object(id)

Returns the association with a given identifier

An association connects, at a minimum, two things, designated subject and object, via some relationship. Associations also include evidence, provenance etc.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
id = 'id_example' # str | identifier for an association, e.g. f5ba436c-f851-41b3-9d9d-bb2b5fc879d4

try:
    # Returns the association with a given identifier
    api_response = api_instance.get_association_object(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier for an association, e.g. f5ba436c-f851-41b3-9d9d-bb2b5fc879d4 | 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations_between**
> list[AssociationResults] get_associations_between(object, subject, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations)

Returns associations connecting two entities

Given two entities (e.g. a particular gene and a particular disease), if these two entities are connected (directly or indirectly), then return the association objects describing the connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
object = 'object_example' # str | Return associations pointing to this node, e.g. MP:0013765. Can also be a biological entity such as a gene
subject = 'subject_example' # str | Return associations emanating from this node, e.g. MGI:1342287 (If ID is from an ontology then results would include inferred associations, by default)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)

try:
    # Returns associations connecting two entities
    api_response = api_instance.get_associations_between(object, subject, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_associations_between: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Return associations pointing to this node, e.g. MP:0013765. Can also be a biological entity such as a gene | 
 **subject** | **str**| Return associations emanating from this node, e.g. MGI:1342287 (If ID is from an ontology then results would include inferred associations, by default) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations_from**
> list[AssociationResults] get_associations_from(subject, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, object_taxon=object_taxon, relation=relation)

Returns list of matching associations starting from a given subject (source)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
subject = 'subject_example' # str | Return associations emanating from this node, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357 (If ID is from an ontology then results would include inferred associations, by default)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
object_taxon = 'object_taxon_example' # str | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) (optional)
relation = 'relation_example' # str | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. (optional)

try:
    # Returns list of matching associations starting from a given subject (source)
    api_response = api_instance.get_associations_from(subject, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations, object_taxon=object_taxon, relation=relation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_associations_from: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Return associations emanating from this node, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357 (If ID is from an ontology then results would include inferred associations, by default) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **object_taxon** | **str**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] 
 **relation** | **str**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations_to**
> list[AssociationResults] get_associations_to(object, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations)

Returns list of matching associations pointing to a given object (target)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
object = 'object_example' # str | Return associations pointing to this node, e.g. specifying MP:0013765 will return all genes, variants, strains, etc. annotated with this term. Can also be a biological entity such as a gene
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)

try:
    # Returns list of matching associations pointing to a given object (target)
    api_response = api_instance.get_associations_to(object, rows=rows, start=start, evidence=evidence, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, use_compact_associations=use_compact_associations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_associations_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Return associations pointing to this node, e.g. specifying MP:0013765 will return all genes, variants, strains, etc. annotated with this term. Can also be a biological entity such as a gene | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

