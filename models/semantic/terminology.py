# Auto generated from terminology.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-02T17:09:59
# Schema: terminology
#
# id: https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/')


# Types

# Class references



@dataclass
class Term(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Term")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Term")

    name_of_location: str = None
    ontology_identifier: Optional[str] = None
    other_anatomical_relations: Optional[str] = None
    parent_structure: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_of_location):
            self.MissingRequiredField("name_of_location")
        if not isinstance(self.name_of_location, str):
            self.name_of_location = str(self.name_of_location)

        if self.ontology_identifier is not None and not isinstance(self.ontology_identifier, str):
            self.ontology_identifier = str(self.ontology_identifier)

        if self.other_anatomical_relations is not None and not isinstance(self.other_anatomical_relations, str):
            self.other_anatomical_relations = str(self.other_anatomical_relations)

        if self.parent_structure is not None and not isinstance(self.parent_structure, str):
            self.parent_structure = str(self.parent_structure)

        super().__post_init__(**kwargs)


@dataclass
class Terminology(YAMLRoot):
    """
    A set of terms that identifies the annotations, providing human readability and context, and allowing
    communication about brain locations and structural properties
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Terminology")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Terminology"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Terminology")

    full_name: str = None
    short_name: str = None
    terms: Union[Union[dict, Term], List[Union[dict, Term]]] = None
    controlled_vocabulary: Union[bool, Bool] = None
    taxonomy: Union[bool, Bool] = None
    ontology: Union[bool, Bool] = None
    defined_in: Optional[str] = None
    ontology_identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.full_name):
            self.MissingRequiredField("full_name")
        if not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self._is_empty(self.short_name):
            self.MissingRequiredField("short_name")
        if not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self._is_empty(self.terms):
            self.MissingRequiredField("terms")
        if not isinstance(self.terms, list):
            self.terms = [self.terms] if self.terms is not None else []
        self.terms = [v if isinstance(v, Term) else Term(**as_dict(v)) for v in self.terms]

        if self._is_empty(self.controlled_vocabulary):
            self.MissingRequiredField("controlled_vocabulary")
        if not isinstance(self.controlled_vocabulary, Bool):
            self.controlled_vocabulary = Bool(self.controlled_vocabulary)

        if self._is_empty(self.taxonomy):
            self.MissingRequiredField("taxonomy")
        if not isinstance(self.taxonomy, Bool):
            self.taxonomy = Bool(self.taxonomy)

        if self._is_empty(self.ontology):
            self.MissingRequiredField("ontology")
        if not isinstance(self.ontology, Bool):
            self.ontology = Bool(self.ontology)

        if self.defined_in is not None and not isinstance(self.defined_in, str):
            self.defined_in = str(self.defined_in)

        if self.ontology_identifier is not None and not isinstance(self.ontology_identifier, str):
            self.ontology_identifier = str(self.ontology_identifier)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.term__name_of_location = Slot(uri=DEFAULT_.name_of_location, name="term__name_of_location", curie=DEFAULT_.curie('name_of_location'),
                   model_uri=DEFAULT_.term__name_of_location, domain=None, range=str)

slots.term__ontology_identifier = Slot(uri=DEFAULT_.ontology_identifier, name="term__ontology_identifier", curie=DEFAULT_.curie('ontology_identifier'),
                   model_uri=DEFAULT_.term__ontology_identifier, domain=None, range=Optional[str])

slots.term__other_anatomical_relations = Slot(uri=DEFAULT_.other_anatomical_relations, name="term__other_anatomical_relations", curie=DEFAULT_.curie('other_anatomical_relations'),
                   model_uri=DEFAULT_.term__other_anatomical_relations, domain=None, range=Optional[str])

slots.term__parent_structure = Slot(uri=DEFAULT_.parent_structure, name="term__parent_structure", curie=DEFAULT_.curie('parent_structure'),
                   model_uri=DEFAULT_.term__parent_structure, domain=None, range=Optional[str])

slots.terminology__full_name = Slot(uri=DEFAULT_.full_name, name="terminology__full_name", curie=DEFAULT_.curie('full_name'),
                   model_uri=DEFAULT_.terminology__full_name, domain=None, range=str)

slots.terminology__short_name = Slot(uri=DEFAULT_.short_name, name="terminology__short_name", curie=DEFAULT_.curie('short_name'),
                   model_uri=DEFAULT_.terminology__short_name, domain=None, range=str)

slots.terminology__terms = Slot(uri=DEFAULT_.terms, name="terminology__terms", curie=DEFAULT_.curie('terms'),
                   model_uri=DEFAULT_.terminology__terms, domain=None, range=Union[Union[dict, Term], List[Union[dict, Term]]])

slots.terminology__defined_in = Slot(uri=DEFAULT_.defined_in, name="terminology__defined_in", curie=DEFAULT_.curie('defined_in'),
                   model_uri=DEFAULT_.terminology__defined_in, domain=None, range=Optional[str])

slots.terminology__ontology_identifier = Slot(uri=DEFAULT_.ontology_identifier, name="terminology__ontology_identifier", curie=DEFAULT_.curie('ontology_identifier'),
                   model_uri=DEFAULT_.terminology__ontology_identifier, domain=None, range=Optional[str])

slots.terminology__controlled_vocabulary = Slot(uri=DEFAULT_.controlled_vocabulary, name="terminology__controlled_vocabulary", curie=DEFAULT_.curie('controlled_vocabulary'),
                   model_uri=DEFAULT_.terminology__controlled_vocabulary, domain=None, range=Union[bool, Bool])

slots.terminology__taxonomy = Slot(uri=DEFAULT_.taxonomy, name="terminology__taxonomy", curie=DEFAULT_.curie('taxonomy'),
                   model_uri=DEFAULT_.terminology__taxonomy, domain=None, range=Union[bool, Bool])

slots.terminology__ontology = Slot(uri=DEFAULT_.ontology, name="terminology__ontology", curie=DEFAULT_.curie('ontology'),
                   model_uri=DEFAULT_.terminology__ontology, domain=None, range=Union[bool, Bool])
