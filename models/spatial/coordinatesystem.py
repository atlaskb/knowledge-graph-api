# Auto generated from coordinatesystem.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-02T16:41:48
# Schema: coordinatesystem
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
from linkml_runtime.linkml_model.types import Date, String
from linkml_runtime.utils.metamodelcore import XSDDate

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
class ThreeDimensionalCartesian(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/ThreeDimensionalCartesian")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ThreeDimensionalCartesian"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/ThreeDimensionalCartesian")

    full_name: str = None
    short_name: str = None
    native_unit: str = None
    origin: str = None
    anatomical_axes_representation: str = None
    release_date: Union[str, XSDDate] = None
    version_information: str = None
    default_image: Optional[str] = None
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

        if self._is_empty(self.native_unit):
            self.MissingRequiredField("native_unit")
        if not isinstance(self.native_unit, str):
            self.native_unit = str(self.native_unit)

        if self._is_empty(self.origin):
            self.MissingRequiredField("origin")
        if not isinstance(self.origin, str):
            self.origin = str(self.origin)

        if self._is_empty(self.anatomical_axes_representation):
            self.MissingRequiredField("anatomical_axes_representation")
        if not isinstance(self.anatomical_axes_representation, str):
            self.anatomical_axes_representation = str(self.anatomical_axes_representation)

        if self._is_empty(self.release_date):
            self.MissingRequiredField("release_date")
        if not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self._is_empty(self.version_information):
            self.MissingRequiredField("version_information")
        if not isinstance(self.version_information, str):
            self.version_information = str(self.version_information)

        if self.default_image is not None and not isinstance(self.default_image, str):
            self.default_image = str(self.default_image)

        if self.ontology_identifier is not None and not isinstance(self.ontology_identifier, str):
            self.ontology_identifier = str(self.ontology_identifier)

        super().__post_init__(**kwargs)


@dataclass
class CoordinateSystem(YAMLRoot):
    """
    A framework for specifying locations with units, origin, direction, and orientation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/CoordinateSystem")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CoordinateSystem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/CoordinateSystem")

    threedimensionalcartesian: Union[dict, ThreeDimensionalCartesian] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.threedimensionalcartesian):
            self.MissingRequiredField("threedimensionalcartesian")
        if not isinstance(self.threedimensionalcartesian, ThreeDimensionalCartesian):
            self.threedimensionalcartesian = ThreeDimensionalCartesian(**as_dict(self.threedimensionalcartesian))

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.threeDimensionalCartesian__full_name = Slot(uri=DEFAULT_.full_name, name="threeDimensionalCartesian__full_name", curie=DEFAULT_.curie('full_name'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__full_name, domain=None, range=str)

slots.threeDimensionalCartesian__short_name = Slot(uri=DEFAULT_.short_name, name="threeDimensionalCartesian__short_name", curie=DEFAULT_.curie('short_name'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__short_name, domain=None, range=str)

slots.threeDimensionalCartesian__native_unit = Slot(uri=DEFAULT_.native_unit, name="threeDimensionalCartesian__native_unit", curie=DEFAULT_.curie('native_unit'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__native_unit, domain=None, range=str)

slots.threeDimensionalCartesian__origin = Slot(uri=DEFAULT_.origin, name="threeDimensionalCartesian__origin", curie=DEFAULT_.curie('origin'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__origin, domain=None, range=str)

slots.threeDimensionalCartesian__anatomical_axes_representation = Slot(uri=DEFAULT_.anatomical_axes_representation, name="threeDimensionalCartesian__anatomical_axes_representation", curie=DEFAULT_.curie('anatomical_axes_representation'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__anatomical_axes_representation, domain=None, range=str)

slots.threeDimensionalCartesian__release_date = Slot(uri=DEFAULT_.release_date, name="threeDimensionalCartesian__release_date", curie=DEFAULT_.curie('release_date'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__release_date, domain=None, range=Union[str, XSDDate])

slots.threeDimensionalCartesian__version_information = Slot(uri=DEFAULT_.version_information, name="threeDimensionalCartesian__version_information", curie=DEFAULT_.curie('version_information'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__version_information, domain=None, range=str)

slots.threeDimensionalCartesian__default_image = Slot(uri=DEFAULT_.default_image, name="threeDimensionalCartesian__default_image", curie=DEFAULT_.curie('default_image'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__default_image, domain=None, range=Optional[str])

slots.threeDimensionalCartesian__ontology_identifier = Slot(uri=DEFAULT_.ontology_identifier, name="threeDimensionalCartesian__ontology_identifier", curie=DEFAULT_.curie('ontology_identifier'),
                   model_uri=DEFAULT_.threeDimensionalCartesian__ontology_identifier, domain=None, range=Optional[str])

slots.coordinateSystem__threedimensionalcartesian = Slot(uri=DEFAULT_.threedimensionalcartesian, name="coordinateSystem__threedimensionalcartesian", curie=DEFAULT_.curie('threedimensionalcartesian'),
                   model_uri=DEFAULT_.coordinateSystem__threedimensionalcartesian, domain=None, range=Union[dict, ThreeDimensionalCartesian])
