from dandischema import DandiBaseModel


class BioSample(DandiBaseModel):
    """Description of the sample that was studied"""

    identifier: Identifier = Field(nskey="schema")
    sampleType: SampleType = Field(
        description="Identifier for the sample characteristics (e.g., from OBI, Encode).",
        nskey="dandi",
    )
    assayType: Optional[List[AssayType]] = Field(
        None, description="Identifier for the assay(s) used (e.g., OBI).", nskey="dandi"
    )
    anatomy: Optional[List[Anatomy]] = Field(
        None,
        description="Identifier for what organ the sample belongs "
                    "to. Use the most specific descriptor from sources such as UBERON.",
        nskey="dandi",
    )

    wasDerivedFrom: Optional[List["BioSample"]] = Field(
        None,
        description="Describes the hierarchy of sample derivation or aggregation.",
        nskey="prov",
    )
    wasAttributedTo: Optional[List[Participant]] = Field(
        None,
        description="Participant(s) or Subject(s) associated with this sample.",
        nskey="prov",
    )
    sameAs: Optional[List[Identifier]] = Field(None, nskey="schema")
    hasMember: Optional[List[Identifier]] = Field(None, nskey="prov")

    _ldmeta = {
        "rdfs:subClassOf": ["schema:Thing", "prov:Entity"],
        "rdfs:label": "Information about the biosample.",
        "nskey": "dandi",
    }