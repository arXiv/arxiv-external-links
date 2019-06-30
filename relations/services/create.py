"""Service for new relation creation."""

from domain import ArXivID, Relation, RelationID, RelationType
from typing import Optional


def create(arxiv_id: ArXivID,
           arxiv_ver: int,
           relation_id: Optional[RelationID],
           relation_type: RelationType,
           resource_type: str,
           resource_id: str,
           description: str,
           creator: str) -> Relation:
    """
    Create a new relation for an e-print.

    Parameters
    ----------
    arxiv_id: ArXivID
        The arXiv ID of the e-print.

    arxiv_ver: int
        The version of the e-print.

    relation_id: RelationID
        THe relation ID to be superceded.

    relation_type: RelationType
        THe type of this relation i.e., ADD, EDIT, or SUPPRESS.

    resource_type: str
        The type of the corresponding resource.

    resource_id: str
        An identifier of the resource e.g., DOI.

    description: str
        A description for the relation.

    creator: str
        Info of the user/app who requested this relation creation.

    Returns
    -------
    Relation
        The newly-created relations.

    """
    pass  # not implemented yet