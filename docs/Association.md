# Association

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Association/annotation unique ID | 
**type** | **str** | Type of association, e.g. gene-phenotype | [optional] 
**subject** | **AllOfAssociationSubject** | Subject of association (what it is about), e.g. ClinVar:nnn, MGI:1201606 | 
**subject_eq** | **list[str]** | Equivalent identifiers to subject node | [optional] 
**subject_extensions** | **list[AllOfAssociationSubjectExtensionsItems]** |  | [optional] 
**object** | **AllOfAssociationObject** | Object (sensu RDF), aka target, e.g. HP:0000448, MP:0002109, DOID:14330 | 
**object_eq** | **list[str]** | Equivalent identifiers to object node | [optional] 
**object_extensions** | **list[AllOfAssociationObjectExtensionsItems]** |  | [optional] 
**relation** | **AllOfAssociationRelation** | Relationship type connecting subject and object | 
**slim** | **list[str]** | Objects mapped to a slim | [optional] 
**negated** | **bool** | True if association is negated | [optional] 
**qualifiers** | **list[str]** | Qualifier on the association | [optional] 
**evidence_graph** | **AllOfAssociationEvidenceGraph** | An indirect association is a join between two or more direct assocations, e.g. gene to disease via ortholog. We record the full set of associations as a graph object | [optional] 
**evidence_types** | [**list[EntityReference]**](EntityReference.md) | Evidence types (ECO classes) | [optional] 
**provided_by** | **list[str]** | Provider of association, e.g. Orphanet, ClinVar | [optional] 
**publications** | [**list[EntityReference]**](EntityReference.md) | Publications supporting association, extracted from evidence graph | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

