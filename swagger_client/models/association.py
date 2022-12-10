# coding: utf-8

"""
    BioLink API

    API integration layer for linked biological objects.   __Source:__ https://github.com/biolink/biolink-api/  # noqa: E501

    OpenAPI spec version: 1.1.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Association(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'type': 'str',
        'subject': 'AllOfAssociationSubject',
        'subject_eq': 'list[str]',
        'subject_extensions': 'list[AllOfAssociationSubjectExtensionsItems]',
        'object': 'AllOfAssociationObject',
        'object_eq': 'list[str]',
        'object_extensions': 'list[AllOfAssociationObjectExtensionsItems]',
        'relation': 'AllOfAssociationRelation',
        'slim': 'list[str]',
        'negated': 'bool',
        'qualifiers': 'list[str]',
        'evidence_graph': 'AllOfAssociationEvidenceGraph',
        'evidence_types': 'list[EntityReference]',
        'provided_by': 'list[str]',
        'publications': 'list[EntityReference]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'subject': 'subject',
        'subject_eq': 'subject_eq',
        'subject_extensions': 'subject_extensions',
        'object': 'object',
        'object_eq': 'object_eq',
        'object_extensions': 'object_extensions',
        'relation': 'relation',
        'slim': 'slim',
        'negated': 'negated',
        'qualifiers': 'qualifiers',
        'evidence_graph': 'evidence_graph',
        'evidence_types': 'evidence_types',
        'provided_by': 'provided_by',
        'publications': 'publications'
    }

    def __init__(self, id=None, type=None, subject=None, subject_eq=None, subject_extensions=None, object=None, object_eq=None, object_extensions=None, relation=None, slim=None, negated=None, qualifiers=None, evidence_graph=None, evidence_types=None, provided_by=None, publications=None):  # noqa: E501
        """Association - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._subject = None
        self._subject_eq = None
        self._subject_extensions = None
        self._object = None
        self._object_eq = None
        self._object_extensions = None
        self._relation = None
        self._slim = None
        self._negated = None
        self._qualifiers = None
        self._evidence_graph = None
        self._evidence_types = None
        self._provided_by = None
        self._publications = None
        self.discriminator = None
        self.id = id
        if type is not None:
            self.type = type
        self.subject = subject
        if subject_eq is not None:
            self.subject_eq = subject_eq
        if subject_extensions is not None:
            self.subject_extensions = subject_extensions
        self.object = object
        if object_eq is not None:
            self.object_eq = object_eq
        if object_extensions is not None:
            self.object_extensions = object_extensions
        self.relation = relation
        if slim is not None:
            self.slim = slim
        if negated is not None:
            self.negated = negated
        if qualifiers is not None:
            self.qualifiers = qualifiers
        if evidence_graph is not None:
            self.evidence_graph = evidence_graph
        if evidence_types is not None:
            self.evidence_types = evidence_types
        if provided_by is not None:
            self.provided_by = provided_by
        if publications is not None:
            self.publications = publications

    @property
    def id(self):
        """Gets the id of this Association.  # noqa: E501

        Association/annotation unique ID  # noqa: E501

        :return: The id of this Association.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Association.

        Association/annotation unique ID  # noqa: E501

        :param id: The id of this Association.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Association.  # noqa: E501

        Type of association, e.g. gene-phenotype  # noqa: E501

        :return: The type of this Association.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Association.

        Type of association, e.g. gene-phenotype  # noqa: E501

        :param type: The type of this Association.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def subject(self):
        """Gets the subject of this Association.  # noqa: E501

        Subject of association (what it is about), e.g. ClinVar:nnn, MGI:1201606  # noqa: E501

        :return: The subject of this Association.  # noqa: E501
        :rtype: AllOfAssociationSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Association.

        Subject of association (what it is about), e.g. ClinVar:nnn, MGI:1201606  # noqa: E501

        :param subject: The subject of this Association.  # noqa: E501
        :type: AllOfAssociationSubject
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def subject_eq(self):
        """Gets the subject_eq of this Association.  # noqa: E501

        Equivalent identifiers to subject node  # noqa: E501

        :return: The subject_eq of this Association.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_eq

    @subject_eq.setter
    def subject_eq(self, subject_eq):
        """Sets the subject_eq of this Association.

        Equivalent identifiers to subject node  # noqa: E501

        :param subject_eq: The subject_eq of this Association.  # noqa: E501
        :type: list[str]
        """

        self._subject_eq = subject_eq

    @property
    def subject_extensions(self):
        """Gets the subject_extensions of this Association.  # noqa: E501


        :return: The subject_extensions of this Association.  # noqa: E501
        :rtype: list[AllOfAssociationSubjectExtensionsItems]
        """
        return self._subject_extensions

    @subject_extensions.setter
    def subject_extensions(self, subject_extensions):
        """Sets the subject_extensions of this Association.


        :param subject_extensions: The subject_extensions of this Association.  # noqa: E501
        :type: list[AllOfAssociationSubjectExtensionsItems]
        """

        self._subject_extensions = subject_extensions

    @property
    def object(self):
        """Gets the object of this Association.  # noqa: E501

        Object (sensu RDF), aka target, e.g. HP:0000448, MP:0002109, DOID:14330  # noqa: E501

        :return: The object of this Association.  # noqa: E501
        :rtype: AllOfAssociationObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Association.

        Object (sensu RDF), aka target, e.g. HP:0000448, MP:0002109, DOID:14330  # noqa: E501

        :param object: The object of this Association.  # noqa: E501
        :type: AllOfAssociationObject
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501

        self._object = object

    @property
    def object_eq(self):
        """Gets the object_eq of this Association.  # noqa: E501

        Equivalent identifiers to object node  # noqa: E501

        :return: The object_eq of this Association.  # noqa: E501
        :rtype: list[str]
        """
        return self._object_eq

    @object_eq.setter
    def object_eq(self, object_eq):
        """Sets the object_eq of this Association.

        Equivalent identifiers to object node  # noqa: E501

        :param object_eq: The object_eq of this Association.  # noqa: E501
        :type: list[str]
        """

        self._object_eq = object_eq

    @property
    def object_extensions(self):
        """Gets the object_extensions of this Association.  # noqa: E501


        :return: The object_extensions of this Association.  # noqa: E501
        :rtype: list[AllOfAssociationObjectExtensionsItems]
        """
        return self._object_extensions

    @object_extensions.setter
    def object_extensions(self, object_extensions):
        """Sets the object_extensions of this Association.


        :param object_extensions: The object_extensions of this Association.  # noqa: E501
        :type: list[AllOfAssociationObjectExtensionsItems]
        """

        self._object_extensions = object_extensions

    @property
    def relation(self):
        """Gets the relation of this Association.  # noqa: E501

        Relationship type connecting subject and object  # noqa: E501

        :return: The relation of this Association.  # noqa: E501
        :rtype: AllOfAssociationRelation
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this Association.

        Relationship type connecting subject and object  # noqa: E501

        :param relation: The relation of this Association.  # noqa: E501
        :type: AllOfAssociationRelation
        """
        if relation is None:
            raise ValueError("Invalid value for `relation`, must not be `None`")  # noqa: E501

        self._relation = relation

    @property
    def slim(self):
        """Gets the slim of this Association.  # noqa: E501

        Objects mapped to a slim  # noqa: E501

        :return: The slim of this Association.  # noqa: E501
        :rtype: list[str]
        """
        return self._slim

    @slim.setter
    def slim(self, slim):
        """Sets the slim of this Association.

        Objects mapped to a slim  # noqa: E501

        :param slim: The slim of this Association.  # noqa: E501
        :type: list[str]
        """

        self._slim = slim

    @property
    def negated(self):
        """Gets the negated of this Association.  # noqa: E501

        True if association is negated  # noqa: E501

        :return: The negated of this Association.  # noqa: E501
        :rtype: bool
        """
        return self._negated

    @negated.setter
    def negated(self, negated):
        """Sets the negated of this Association.

        True if association is negated  # noqa: E501

        :param negated: The negated of this Association.  # noqa: E501
        :type: bool
        """

        self._negated = negated

    @property
    def qualifiers(self):
        """Gets the qualifiers of this Association.  # noqa: E501

        Qualifier on the association  # noqa: E501

        :return: The qualifiers of this Association.  # noqa: E501
        :rtype: list[str]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers):
        """Sets the qualifiers of this Association.

        Qualifier on the association  # noqa: E501

        :param qualifiers: The qualifiers of this Association.  # noqa: E501
        :type: list[str]
        """

        self._qualifiers = qualifiers

    @property
    def evidence_graph(self):
        """Gets the evidence_graph of this Association.  # noqa: E501

        An indirect association is a join between two or more direct assocations, e.g. gene to disease via ortholog. We record the full set of associations as a graph object  # noqa: E501

        :return: The evidence_graph of this Association.  # noqa: E501
        :rtype: AllOfAssociationEvidenceGraph
        """
        return self._evidence_graph

    @evidence_graph.setter
    def evidence_graph(self, evidence_graph):
        """Sets the evidence_graph of this Association.

        An indirect association is a join between two or more direct assocations, e.g. gene to disease via ortholog. We record the full set of associations as a graph object  # noqa: E501

        :param evidence_graph: The evidence_graph of this Association.  # noqa: E501
        :type: AllOfAssociationEvidenceGraph
        """

        self._evidence_graph = evidence_graph

    @property
    def evidence_types(self):
        """Gets the evidence_types of this Association.  # noqa: E501

        Evidence types (ECO classes)  # noqa: E501

        :return: The evidence_types of this Association.  # noqa: E501
        :rtype: list[EntityReference]
        """
        return self._evidence_types

    @evidence_types.setter
    def evidence_types(self, evidence_types):
        """Sets the evidence_types of this Association.

        Evidence types (ECO classes)  # noqa: E501

        :param evidence_types: The evidence_types of this Association.  # noqa: E501
        :type: list[EntityReference]
        """

        self._evidence_types = evidence_types

    @property
    def provided_by(self):
        """Gets the provided_by of this Association.  # noqa: E501

        Provider of association, e.g. Orphanet, ClinVar  # noqa: E501

        :return: The provided_by of this Association.  # noqa: E501
        :rtype: list[str]
        """
        return self._provided_by

    @provided_by.setter
    def provided_by(self, provided_by):
        """Sets the provided_by of this Association.

        Provider of association, e.g. Orphanet, ClinVar  # noqa: E501

        :param provided_by: The provided_by of this Association.  # noqa: E501
        :type: list[str]
        """

        self._provided_by = provided_by

    @property
    def publications(self):
        """Gets the publications of this Association.  # noqa: E501

        Publications supporting association, extracted from evidence graph  # noqa: E501

        :return: The publications of this Association.  # noqa: E501
        :rtype: list[EntityReference]
        """
        return self._publications

    @publications.setter
    def publications(self, publications):
        """Sets the publications of this Association.

        Publications supporting association, extracted from evidence graph  # noqa: E501

        :param publications: The publications of this Association.  # noqa: E501
        :type: list[EntityReference]
        """

        self._publications = publications

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Association, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Association):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other