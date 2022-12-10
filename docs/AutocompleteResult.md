# AutocompleteResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | curie formatted id | [optional] 
**label** | **list[str]** | primary label (rdfs:label) | [optional] 
**match** | **str** | matched part of document (may be primary label, synonym, id, etc) | [optional] 
**category** | **list[str]** | node categories | [optional] 
**taxon** | **str** | taxon as NCBITaxon curie | [optional] 
**taxon_label** | **str** | taxon label | [optional] 
**highlight** | **str** | solr highlight | [optional] 
**has_highlight** | **bool** | True if highlight can be interpreted as html, else False | [optional] 
**equivalent_ids** | **list[str]** | Equivalent IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

