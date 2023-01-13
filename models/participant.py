from dandischema import DandiBaseModel


class Participant(DandiBaseModel):
    """Description about the Participant or Subject studied.
    The Participant or Subject can be any individual or synthesized Agent. The
    properties of the Participant or Subject refers to information at the timepoint
    when the Participant or Subject engaged in the production of data being described.
    """

    identifier: Identifier = Field(nskey="schema")
    altName: Optional[List[Identifier]] = Field(None, nskey="dandi")

    strain: Optional[StrainType] = Field(
        None,
        description="Identifier for the strain of the participant or subject.",
        nskey="dandi",
    )
    cellLine: Optional[Identifier] = Field(
        None,
        description="Cell line associated with the participant or subject.",
        nskey="dandi",
    )
    vendor: Optional[Organization] = Field(None, nskey="dandi")
    age: Optional[PropertyValue] = Field(
        None,
        description="A representation of age using ISO 8601 duration. This "
                    "should include a valueReference if anything other than "
                    "date of birth is used.",
        nskey="dandi",
        rangeIncludes="schema:Duration",
    )

    sex: Optional[SexType] = Field(
        None,
        description="Identifier for sex of the participant or subject if "
                    "available. (e.g. from OBI)",
        nskey="dandi",
    )
    genotype: Optional[Union[List[GenotypeInfo], Identifier]] = Field(
        None,
        description="Genotype descriptor of participant or subject if available",
        nskey="dandi",
    )
    species: Optional[SpeciesType] = Field(
        None,
        description="An identifier indicating the taxonomic classification of "
                    "the participant or subject.",
        nskey="dandi",
    )
    disorder: Optional[List[Disorder]] = Field(
        None,
        description="Any current diagnosed disease or disorder associated with "
                    "the participant or subject.",
        nskey="dandi",
    )

    relatedParticipant: Optional[List[RelatedParticipant]] = Field(
        None,
        description="Information about related participants or subjects in a "
                    "study or across studies.",
        nskey="dandi",
    )
    sameAs: Optional[List[Identifier]] = Field(
        None,
        description="An identifier to link participants or subjects across datasets.",
        nskey="schema",
    )

    _ldmeta = {
        "rdfs:subClassOf": ["prov:Agent"],
        "rdfs:label": "Information about the participant or subject.",
        "nskey": "dandi",
    }
