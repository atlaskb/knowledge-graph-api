# Auto generated from annotationset.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-02T17:09:32
# Schema: annotationset
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
class Annotation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Annotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Annotation")

    internal_identifier: str = None
    laterality: str = None
    criteria_type: str = None
    visualized_in: str = None
    criteria: Optional[str] = None
    display_color: Optional[str] = None
    inspired_by: Optional[str] = None
    best_view_point: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.internal_identifier):
            self.MissingRequiredField("internal_identifier")
        if not isinstance(self.internal_identifier, str):
            self.internal_identifier = str(self.internal_identifier)

        if self._is_empty(self.laterality):
            self.MissingRequiredField("laterality")
        if not isinstance(self.laterality, str):
            self.laterality = str(self.laterality)

        if self._is_empty(self.criteria_type):
            self.MissingRequiredField("criteria_type")
        if not isinstance(self.criteria_type, str):
            self.criteria_type = str(self.criteria_type)

        if self._is_empty(self.visualized_in):
            self.MissingRequiredField("visualized_in")
        if not isinstance(self.visualized_in, str):
            self.visualized_in = str(self.visualized_in)

        if self.criteria is not None and not isinstance(self.criteria, str):
            self.criteria = str(self.criteria)

        if self.display_color is not None and not isinstance(self.display_color, str):
            self.display_color = str(self.display_color)

        if self.inspired_by is not None and not isinstance(self.inspired_by, str):
            self.inspired_by = str(self.inspired_by)

        if self.best_view_point is not None and not isinstance(self.best_view_point, str):
            self.best_view_point = str(self.best_view_point)

        super().__post_init__(**kwargs)


@dataclass
class AnnotationSet(YAMLRoot):
    """
    Graphical marks or labels referring to spatial locations determined by features observed in, inferred from, or
    mapped onto the reference data, specifying structures or boundaries
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/AnnotationSet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnnotationSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/AnnotationSet")

    full_name: str = None
    short_name: str = None
    annotations: Union[Union[dict, Annotation], List[Union[dict, Annotation]]] = None
    delineation: Union[bool, Bool] = None
    parcellation: Union[bool, Bool] = None
    probabilistic_map: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.full_name):
            self.MissingRequiredField("full_name")
        if not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self._is_empty(self.short_name):
            self.MissingRequiredField("short_name")
        if not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self._is_empty(self.annotations):
            self.MissingRequiredField("annotations")
        if not isinstance(self.annotations, list):
            self.annotations = [self.annotations] if self.annotations is not None else []
        self.annotations = [v if isinstance(v, Annotation) else Annotation(**as_dict(v)) for v in self.annotations]

        if self._is_empty(self.delineation):
            self.MissingRequiredField("delineation")
        if not isinstance(self.delineation, Bool):
            self.delineation = Bool(self.delineation)

        if self._is_empty(self.parcellation):
            self.MissingRequiredField("parcellation")
        if not isinstance(self.parcellation, Bool):
            self.parcellation = Bool(self.parcellation)

        if self._is_empty(self.probabilistic_map):
            self.MissingRequiredField("probabilistic_map")
        if not isinstance(self.probabilistic_map, Bool):
            self.probabilistic_map = Bool(self.probabilistic_map)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.annotation__internal_identifier = Slot(uri=DEFAULT_.internal_identifier, name="annotation__internal_identifier", curie=DEFAULT_.curie('internal_identifier'),
                   model_uri=DEFAULT_.annotation__internal_identifier, domain=None, range=str)

slots.annotation__laterality = Slot(uri=DEFAULT_.laterality, name="annotation__laterality", curie=DEFAULT_.curie('laterality'),
                   model_uri=DEFAULT_.annotation__laterality, domain=None, range=str)

slots.annotation__criteria_type = Slot(uri=DEFAULT_.criteria_type, name="annotation__criteria_type", curie=DEFAULT_.curie('criteria_type'),
                   model_uri=DEFAULT_.annotation__criteria_type, domain=None, range=str)

slots.annotation__visualized_in = Slot(uri=DEFAULT_.visualized_in, name="annotation__visualized_in", curie=DEFAULT_.curie('visualized_in'),
                   model_uri=DEFAULT_.annotation__visualized_in, domain=None, range=str)

slots.annotation__criteria = Slot(uri=DEFAULT_.criteria, name="annotation__criteria", curie=DEFAULT_.curie('criteria'),
                   model_uri=DEFAULT_.annotation__criteria, domain=None, range=Optional[str])

slots.annotation__display_color = Slot(uri=DEFAULT_.display_color, name="annotation__display_color", curie=DEFAULT_.curie('display_color'),
                   model_uri=DEFAULT_.annotation__display_color, domain=None, range=Optional[str])

slots.annotation__inspired_by = Slot(uri=DEFAULT_.inspired_by, name="annotation__inspired_by", curie=DEFAULT_.curie('inspired_by'),
                   model_uri=DEFAULT_.annotation__inspired_by, domain=None, range=Optional[str])

slots.annotation__best_view_point = Slot(uri=DEFAULT_.best_view_point, name="annotation__best_view_point", curie=DEFAULT_.curie('best_view_point'),
                   model_uri=DEFAULT_.annotation__best_view_point, domain=None, range=Optional[str])

slots.annotationSet__full_name = Slot(uri=DEFAULT_.full_name, name="annotationSet__full_name", curie=DEFAULT_.curie('full_name'),
                   model_uri=DEFAULT_.annotationSet__full_name, domain=None, range=str)

slots.annotationSet__short_name = Slot(uri=DEFAULT_.short_name, name="annotationSet__short_name", curie=DEFAULT_.curie('short_name'),
                   model_uri=DEFAULT_.annotationSet__short_name, domain=None, range=str)

slots.annotationSet__annotations = Slot(uri=DEFAULT_.annotations, name="annotationSet__annotations", curie=DEFAULT_.curie('annotations'),
                   model_uri=DEFAULT_.annotationSet__annotations, domain=None, range=Union[Union[dict, Annotation], List[Union[dict, Annotation]]])

slots.annotationSet__delineation = Slot(uri=DEFAULT_.delineation, name="annotationSet__delineation", curie=DEFAULT_.curie('delineation'),
                   model_uri=DEFAULT_.annotationSet__delineation, domain=None, range=Union[bool, Bool])

slots.annotationSet__parcellation = Slot(uri=DEFAULT_.parcellation, name="annotationSet__parcellation", curie=DEFAULT_.curie('parcellation'),
                   model_uri=DEFAULT_.annotationSet__parcellation, domain=None, range=Union[bool, Bool])

slots.annotationSet__probabilistic_map = Slot(uri=DEFAULT_.probabilistic_map, name="annotationSet__probabilistic_map", curie=DEFAULT_.curie('probabilistic_map'),
                   model_uri=DEFAULT_.annotationSet__probabilistic_map, domain=None, range=Union[bool, Bool])
