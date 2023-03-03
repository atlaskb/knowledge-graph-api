# Auto generated from referencedata.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-02T16:50:54
# Schema: referencedata
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
from linkml_runtime.linkml_model.types import Integer, String

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
class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Subject")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Subject")

    identifier: str = None
    species: str = None
    biological_sex: str = None
    method_information: str = None
    processing_information: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self._is_empty(self.species):
            self.MissingRequiredField("species")
        if not isinstance(self.species, str):
            self.species = str(self.species)

        if self._is_empty(self.biological_sex):
            self.MissingRequiredField("biological_sex")
        if not isinstance(self.biological_sex, str):
            self.biological_sex = str(self.biological_sex)

        if self._is_empty(self.method_information):
            self.MissingRequiredField("method_information")
        if not isinstance(self.method_information, str):
            self.method_information = str(self.method_information)

        if self._is_empty(self.processing_information):
            self.MissingRequiredField("processing_information")
        if not isinstance(self.processing_information, str):
            self.processing_information = str(self.processing_information)

        super().__post_init__(**kwargs)


@dataclass
class Image(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Image")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/Image")

    defined_in: str = None
    voxel_or_pixel_size: int = None
    coordinate_space: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.defined_in):
            self.MissingRequiredField("defined_in")
        if not isinstance(self.defined_in, str):
            self.defined_in = str(self.defined_in)

        if self._is_empty(self.voxel_or_pixel_size):
            self.MissingRequiredField("voxel_or_pixel_size")
        if not isinstance(self.voxel_or_pixel_size, int):
            self.voxel_or_pixel_size = int(self.voxel_or_pixel_size)

        if self._is_empty(self.coordinate_space):
            self.MissingRequiredField("coordinate_space")
        if not isinstance(self.coordinate_space, str):
            self.coordinate_space = str(self.coordinate_space)

        super().__post_init__(**kwargs)


@dataclass
class ReferenceData(YAMLRoot):
    """
    Graphical representations of one or several brains, or parts of brains, chosen as the biological reference for
    that atlas
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/ReferenceData")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReferenceData"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/ReferenceData")

    subjects: Union[Union[dict, Subject], List[Union[dict, Subject]]] = None
    image: Union[dict, Image] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        if not isinstance(self.subjects, list):
            self.subjects = [self.subjects] if self.subjects is not None else []
        self.subjects = [v if isinstance(v, Subject) else Subject(**as_dict(v)) for v in self.subjects]

        if self._is_empty(self.image):
            self.MissingRequiredField("image")
        if not isinstance(self.image, Image):
            self.image = Image(**as_dict(self.image))

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.subject__identifier = Slot(uri=DEFAULT_.identifier, name="subject__identifier", curie=DEFAULT_.curie('identifier'),
                   model_uri=DEFAULT_.subject__identifier, domain=None, range=str)

slots.subject__species = Slot(uri=DEFAULT_.species, name="subject__species", curie=DEFAULT_.curie('species'),
                   model_uri=DEFAULT_.subject__species, domain=None, range=str)

slots.subject__biological_sex = Slot(uri=DEFAULT_.biological_sex, name="subject__biological_sex", curie=DEFAULT_.curie('biological_sex'),
                   model_uri=DEFAULT_.subject__biological_sex, domain=None, range=str)

slots.subject__method_information = Slot(uri=DEFAULT_.method_information, name="subject__method_information", curie=DEFAULT_.curie('method_information'),
                   model_uri=DEFAULT_.subject__method_information, domain=None, range=str)

slots.subject__processing_information = Slot(uri=DEFAULT_.processing_information, name="subject__processing_information", curie=DEFAULT_.curie('processing_information'),
                   model_uri=DEFAULT_.subject__processing_information, domain=None, range=str)

slots.image__defined_in = Slot(uri=DEFAULT_.defined_in, name="image__defined_in", curie=DEFAULT_.curie('defined_in'),
                   model_uri=DEFAULT_.image__defined_in, domain=None, range=str)

slots.image__voxel_or_pixel_size = Slot(uri=DEFAULT_.voxel_or_pixel_size, name="image__voxel_or_pixel_size", curie=DEFAULT_.curie('voxel_or_pixel_size'),
                   model_uri=DEFAULT_.image__voxel_or_pixel_size, domain=None, range=int)

slots.image__coordinate_space = Slot(uri=DEFAULT_.coordinate_space, name="image__coordinate_space", curie=DEFAULT_.curie('coordinate_space'),
                   model_uri=DEFAULT_.image__coordinate_space, domain=None, range=str)

slots.referenceData__subjects = Slot(uri=DEFAULT_.subjects, name="referenceData__subjects", curie=DEFAULT_.curie('subjects'),
                   model_uri=DEFAULT_.referenceData__subjects, domain=None, range=Union[Union[dict, Subject], List[Union[dict, Subject]]])

slots.referenceData__image = Slot(uri=DEFAULT_.image, name="referenceData__image", curie=DEFAULT_.curie('image'),
                   model_uri=DEFAULT_.referenceData__image, domain=None, range=Union[dict, Image])
