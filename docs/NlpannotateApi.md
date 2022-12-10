# swagger_client.NlpannotateApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_annotate**](NlpannotateApi.md#get_annotate) | **GET** /nlp/annotate/ | Annotate a given text using SciGraph annotator
[**get_annotate_entities**](NlpannotateApi.md#get_annotate_entities) | **GET** /nlp/annotate/entities | Annotate a given content using SciGraph annotator and get all entities from content
[**post_annotate**](NlpannotateApi.md#post_annotate) | **POST** /nlp/annotate/ | Annotate a given text using SciGraph annotator
[**post_annotate_entities**](NlpannotateApi.md#post_annotate_entities) | **POST** /nlp/annotate/entities | Annotate a given content using SciGraph annotator and get all entities from content

# **get_annotate**
> get_annotate(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)

Annotate a given text using SciGraph annotator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NlpannotateApi()
content = 'content_example' # str | The text content to annotate (optional)
include_category = ['include_category_example'] # list[str] | Categories to include for annotation (optional)
exclude_category = ['exclude_category_example'] # list[str] | Categories to exclude for annotation (optional)
min_length = '4' # str | The minimum number of characters in the annotated entity (optional) (default to 4)
longest_only = false # bool | Should only the longest entity be returned for an overlapping group (optional) (default to false)
include_abbreviation = false # bool | Should abbreviations be included (optional) (default to false)
include_acronym = false # bool | Should acronyms be included (optional) (default to false)
include_numbers = false # bool | Should numbers be included (optional) (default to false)

try:
    # Annotate a given text using SciGraph annotator
    api_instance.get_annotate(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)
except ApiException as e:
    print("Exception when calling NlpannotateApi->get_annotate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| The text content to annotate | [optional] 
 **include_category** | [**list[str]**](str.md)| Categories to include for annotation | [optional] 
 **exclude_category** | [**list[str]**](str.md)| Categories to exclude for annotation | [optional] 
 **min_length** | **str**| The minimum number of characters in the annotated entity | [optional] [default to 4]
 **longest_only** | **bool**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **include_abbreviation** | **bool**| Should abbreviations be included | [optional] [default to false]
 **include_acronym** | **bool**| Should acronyms be included | [optional] [default to false]
 **include_numbers** | **bool**| Should numbers be included | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotate_entities**
> EntityAnnotationResult get_annotate_entities(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)

Annotate a given content using SciGraph annotator and get all entities from content

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NlpannotateApi()
content = 'content_example' # str | The text content to annotate (optional)
include_category = ['include_category_example'] # list[str] | Categories to include for annotation (optional)
exclude_category = ['exclude_category_example'] # list[str] | Categories to exclude for annotation (optional)
min_length = '4' # str | The minimum number of characters in the annotated entity (optional) (default to 4)
longest_only = false # bool | Should only the longest entity be returned for an overlapping group (optional) (default to false)
include_abbreviation = false # bool | Should abbreviations be included (optional) (default to false)
include_acronym = false # bool | Should acronyms be included (optional) (default to false)
include_numbers = false # bool | Should numbers be included (optional) (default to false)

try:
    # Annotate a given content using SciGraph annotator and get all entities from content
    api_response = api_instance.get_annotate_entities(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NlpannotateApi->get_annotate_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| The text content to annotate | [optional] 
 **include_category** | [**list[str]**](str.md)| Categories to include for annotation | [optional] 
 **exclude_category** | [**list[str]**](str.md)| Categories to exclude for annotation | [optional] 
 **min_length** | **str**| The minimum number of characters in the annotated entity | [optional] [default to 4]
 **longest_only** | **bool**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **include_abbreviation** | **bool**| Should abbreviations be included | [optional] [default to false]
 **include_acronym** | **bool**| Should acronyms be included | [optional] [default to false]
 **include_numbers** | **bool**| Should numbers be included | [optional] [default to false]

### Return type

[**EntityAnnotationResult**](EntityAnnotationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_annotate**
> post_annotate(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)

Annotate a given text using SciGraph annotator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NlpannotateApi()
content = 'content_example' # str | The text content to annotate (optional)
include_category = ['include_category_example'] # list[str] | Categories to include for annotation (optional)
exclude_category = ['exclude_category_example'] # list[str] | Categories to exclude for annotation (optional)
min_length = '4' # str | The minimum number of characters in the annotated entity (optional) (default to 4)
longest_only = false # bool | Should only the longest entity be returned for an overlapping group (optional) (default to false)
include_abbreviation = false # bool | Should abbreviations be included (optional) (default to false)
include_acronym = false # bool | Should acronyms be included (optional) (default to false)
include_numbers = false # bool | Should numbers be included (optional) (default to false)

try:
    # Annotate a given text using SciGraph annotator
    api_instance.post_annotate(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)
except ApiException as e:
    print("Exception when calling NlpannotateApi->post_annotate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| The text content to annotate | [optional] 
 **include_category** | [**list[str]**](str.md)| Categories to include for annotation | [optional] 
 **exclude_category** | [**list[str]**](str.md)| Categories to exclude for annotation | [optional] 
 **min_length** | **str**| The minimum number of characters in the annotated entity | [optional] [default to 4]
 **longest_only** | **bool**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **include_abbreviation** | **bool**| Should abbreviations be included | [optional] [default to false]
 **include_acronym** | **bool**| Should acronyms be included | [optional] [default to false]
 **include_numbers** | **bool**| Should numbers be included | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_annotate_entities**
> EntityAnnotationResult post_annotate_entities(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)

Annotate a given content using SciGraph annotator and get all entities from content

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NlpannotateApi()
content = 'content_example' # str | The text content to annotate (optional)
include_category = ['include_category_example'] # list[str] | Categories to include for annotation (optional)
exclude_category = ['exclude_category_example'] # list[str] | Categories to exclude for annotation (optional)
min_length = '4' # str | The minimum number of characters in the annotated entity (optional) (default to 4)
longest_only = false # bool | Should only the longest entity be returned for an overlapping group (optional) (default to false)
include_abbreviation = false # bool | Should abbreviations be included (optional) (default to false)
include_acronym = false # bool | Should acronyms be included (optional) (default to false)
include_numbers = false # bool | Should numbers be included (optional) (default to false)

try:
    # Annotate a given content using SciGraph annotator and get all entities from content
    api_response = api_instance.post_annotate_entities(content=content, include_category=include_category, exclude_category=exclude_category, min_length=min_length, longest_only=longest_only, include_abbreviation=include_abbreviation, include_acronym=include_acronym, include_numbers=include_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NlpannotateApi->post_annotate_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| The text content to annotate | [optional] 
 **include_category** | [**list[str]**](str.md)| Categories to include for annotation | [optional] 
 **exclude_category** | [**list[str]**](str.md)| Categories to exclude for annotation | [optional] 
 **min_length** | **str**| The minimum number of characters in the annotated entity | [optional] [default to 4]
 **longest_only** | **bool**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **include_abbreviation** | **bool**| Should abbreviations be included | [optional] [default to false]
 **include_acronym** | **bool**| Should acronyms be included | [optional] [default to false]
 **include_numbers** | **bool**| Should numbers be included | [optional] [default to false]

### Return type

[**EntityAnnotationResult**](EntityAnnotationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

