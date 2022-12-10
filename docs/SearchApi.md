# swagger_client.SearchApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_autocomplete**](SearchApi.md#get_autocomplete) | **GET** /search/entity/autocomplete/{term} | Returns list of matching concepts or entities using lexical search
[**get_search_entities**](SearchApi.md#get_search_entities) | **GET** /search/entity/{term} | Returns list of matching concepts or entities using lexical search
[**get_search_hpo_entities**](SearchApi.md#get_search_hpo_entities) | **GET** /search/entity/hpo-pl/{term} | Returns list of matching concepts or entities using lexical search

# **get_autocomplete**
> AutocompleteResults get_autocomplete(term, fq=fq, category=category, prefix=prefix, include_eqs=include_eqs, boost_fx=boost_fx, boost_q=boost_q, taxon=taxon, rows=rows, start=start, highlight_class=highlight_class, min_match=min_match, exclude_groups=exclude_groups, minimal_tokenizer=minimal_tokenizer)

Returns list of matching concepts or entities using lexical search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
term = 'term_example' # str | 
fq = ['fq_example'] # list[str] | fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. (optional)
category = ['category_example'] # list[str] | e.g. gene, disease (optional)
prefix = ['prefix_example'] # list[str] | ontology prefix: HP, -MONDO (optional)
include_eqs = false # bool | Include equivalent ids in prefix filter (optional) (default to false)
boost_fx = ['boost_fx_example'] # list[str] | boost function e.g. pow(edges,0.334) (optional)
boost_q = ['boost_q_example'] # list[str] | boost query e.g. category:genotype^-10 (optional)
taxon = ['taxon_example'] # list[str] | taxon filter, eg NCBITaxon:9606, includes inferred taxa (optional)
rows = 20 # int | number of rows (optional) (default to 20)
start = '0' # str | row number to start from (optional) (default to 0)
highlight_class = 'highlight_class_example' # str | highlight class (optional)
min_match = 'min_match_example' # str | minimum should match parameter, see solr docs for details (optional)
exclude_groups = false # bool | Exclude grouping classes (classes with subclasses) (optional) (default to false)
minimal_tokenizer = false # bool | set to true to use the minimal tokenizer, good for variants and genotypes (optional) (default to false)

try:
    # Returns list of matching concepts or entities using lexical search
    api_response = api_instance.get_autocomplete(term, fq=fq, category=category, prefix=prefix, include_eqs=include_eqs, boost_fx=boost_fx, boost_q=boost_q, taxon=taxon, rows=rows, start=start, highlight_class=highlight_class, min_match=min_match, exclude_groups=exclude_groups, minimal_tokenizer=minimal_tokenizer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_autocomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 
 **fq** | [**list[str]**](str.md)| fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. | [optional] 
 **category** | [**list[str]**](str.md)| e.g. gene, disease | [optional] 
 **prefix** | [**list[str]**](str.md)| ontology prefix: HP, -MONDO | [optional] 
 **include_eqs** | **bool**| Include equivalent ids in prefix filter | [optional] [default to false]
 **boost_fx** | [**list[str]**](str.md)| boost function e.g. pow(edges,0.334) | [optional] 
 **boost_q** | [**list[str]**](str.md)| boost query e.g. category:genotype^-10 | [optional] 
 **taxon** | [**list[str]**](str.md)| taxon filter, eg NCBITaxon:9606, includes inferred taxa | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **start** | **str**| row number to start from | [optional] [default to 0]
 **highlight_class** | **str**| highlight class | [optional] 
 **min_match** | **str**| minimum should match parameter, see solr docs for details | [optional] 
 **exclude_groups** | **bool**| Exclude grouping classes (classes with subclasses) | [optional] [default to false]
 **minimal_tokenizer** | **bool**| set to true to use the minimal tokenizer, good for variants and genotypes | [optional] [default to false]

### Return type

[**AutocompleteResults**](AutocompleteResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_entities**
> SearchResult get_search_entities(term, fq=fq, category=category, prefix=prefix, include_eqs=include_eqs, boost_fx=boost_fx, boost_q=boost_q, taxon=taxon, rows=rows, start=start, highlight_class=highlight_class, min_match=min_match, exclude_groups=exclude_groups, minimal_tokenizer=minimal_tokenizer)

Returns list of matching concepts or entities using lexical search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
term = 'term_example' # str | search string, e.g. shh, parkinson, femur
fq = ['fq_example'] # list[str] | fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. (optional)
category = ['category_example'] # list[str] | e.g. gene, disease (optional)
prefix = ['prefix_example'] # list[str] | ontology prefix: HP, -MONDO (optional)
include_eqs = false # bool | Include equivalent ids in prefix filter (optional) (default to false)
boost_fx = ['boost_fx_example'] # list[str] | boost function e.g. pow(edges,0.334) (optional)
boost_q = ['boost_q_example'] # list[str] | boost query e.g. category:genotype^-10 (optional)
taxon = ['taxon_example'] # list[str] | taxon filter, eg NCBITaxon:9606, includes inferred taxa (optional)
rows = 20 # int | number of rows (optional) (default to 20)
start = '0' # str | row number to start from (optional) (default to 0)
highlight_class = 'highlight_class_example' # str | highlight class (optional)
min_match = 'min_match_example' # str | minimum should match parameter, see solr docs for details (optional)
exclude_groups = false # bool | Exclude grouping classes (classes with subclasses) (optional) (default to false)
minimal_tokenizer = false # bool | set to true to use the minimal tokenizer, good for variants and genotypes (optional) (default to false)

try:
    # Returns list of matching concepts or entities using lexical search
    api_response = api_instance.get_search_entities(term, fq=fq, category=category, prefix=prefix, include_eqs=include_eqs, boost_fx=boost_fx, boost_q=boost_q, taxon=taxon, rows=rows, start=start, highlight_class=highlight_class, min_match=min_match, exclude_groups=exclude_groups, minimal_tokenizer=minimal_tokenizer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| search string, e.g. shh, parkinson, femur | 
 **fq** | [**list[str]**](str.md)| fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. | [optional] 
 **category** | [**list[str]**](str.md)| e.g. gene, disease | [optional] 
 **prefix** | [**list[str]**](str.md)| ontology prefix: HP, -MONDO | [optional] 
 **include_eqs** | **bool**| Include equivalent ids in prefix filter | [optional] [default to false]
 **boost_fx** | [**list[str]**](str.md)| boost function e.g. pow(edges,0.334) | [optional] 
 **boost_q** | [**list[str]**](str.md)| boost query e.g. category:genotype^-10 | [optional] 
 **taxon** | [**list[str]**](str.md)| taxon filter, eg NCBITaxon:9606, includes inferred taxa | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **start** | **str**| row number to start from | [optional] [default to 0]
 **highlight_class** | **str**| highlight class | [optional] 
 **min_match** | **str**| minimum should match parameter, see solr docs for details | [optional] 
 **exclude_groups** | **bool**| Exclude grouping classes (classes with subclasses) | [optional] [default to false]
 **minimal_tokenizer** | **bool**| set to true to use the minimal tokenizer, good for variants and genotypes | [optional] [default to false]

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_hpo_entities**
> LayResults get_search_hpo_entities(term, rows=rows, start=start, phenotype_group=phenotype_group, phenotype_group_label=phenotype_group_label, anatomical_system=anatomical_system, anatomical_system_label=anatomical_system_label, highlight_class=highlight_class)

Returns list of matching concepts or entities using lexical search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
term = 'term_example' # str | search string, e.g. muscle atrophy, frequent infections
rows = 10 # int | number of rows (optional) (default to 10)
start = '0' # str | row number to start from (optional) (default to 0)
phenotype_group = 'phenotype_group_example' # str | phenotype group id (optional)
phenotype_group_label = 'phenotype_group_label_example' # str | phenotype group label (optional)
anatomical_system = 'anatomical_system_example' # str | anatomical system id (optional)
anatomical_system_label = 'anatomical_system_label_example' # str | anatomical system label (optional)
highlight_class = 'highlight_class_example' # str | highlight class (optional)

try:
    # Returns list of matching concepts or entities using lexical search
    api_response = api_instance.get_search_hpo_entities(term, rows=rows, start=start, phenotype_group=phenotype_group, phenotype_group_label=phenotype_group_label, anatomical_system=anatomical_system, anatomical_system_label=anatomical_system_label, highlight_class=highlight_class)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search_hpo_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| search string, e.g. muscle atrophy, frequent infections | 
 **rows** | **int**| number of rows | [optional] [default to 10]
 **start** | **str**| row number to start from | [optional] [default to 0]
 **phenotype_group** | **str**| phenotype group id | [optional] 
 **phenotype_group_label** | **str**| phenotype group label | [optional] 
 **anatomical_system** | **str**| anatomical system id | [optional] 
 **anatomical_system_label** | **str**| anatomical system label | [optional] 
 **highlight_class** | **str**| highlight class | [optional] 

### Return type

[**LayResults**](LayResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

