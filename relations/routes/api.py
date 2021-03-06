"""Defines the HTTP routes and methods supported by the relations API."""

from flask import Blueprint, Response, request
from flask.json import jsonify

from .. import controllers


blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/status', methods=['GET'])
def service_status() -> Response:
    """
    Service status endpoint.

    Returns ``200 OK`` if the service is up and ready to handle requests.
    """
    response_data, status_code, headers = controllers.service_status(request.params)
    response: Response = jsonify(response_data)
    response.status_code = status_code
    response.headers.extend(headers)
    return response


@blueprint.route('/<string:arxiv_id_str>v<int:arxiv_ver>/relations', methods=['POST'])
def create_new(arxiv_id_str: str, arxiv_ver: int) -> Response:
    """Create a new relation for an e-print."""
    response_data, status_code, headers = controllers.create_new(arxiv_id_str,
                                                                 arxiv_ver,
                                                                 request.json)
    response: Response = jsonify(response_data)
    response.status_code = status_code
    response.headers.extend(headers)
    return response


@blueprint.route('/<string:arxiv_id_str>v<int:arxiv_ver>/relations/<string:relation_id_str>', methods=['PUT'])
def supercede(arxiv_id_str: str, arxiv_ver: int, relation_id_str: str) -> Response:
    """Create a new relation for an e-print which supersedes an existing relation."""
    response_data, status_code, headers = controllers.supercede(arxiv_id_str,
                                                                arxiv_ver,
                                                                relation_id_str,
                                                                request.json)
    response: Response = jsonify(response_data)
    response.status_code = status_code
    response.headers.extend(headers)
    return response


@blueprint.route('/<string:arxiv_id_str>v<int:arxiv_ver>/relations/<string:relation_id_str>', methods=['DELETE'])
def suppress(arxiv_id_str: str, arxiv_ver: int, relation_id_str: str) -> Response:
    """Create a new relation for an e-print which supresses an existing relation."""
    response_data, status_code, headers = controllers.suppress(arxiv_id_str,
                                                               arxiv_ver,
                                                               relation_id_str,
                                                               request.json)
    response: Response = jsonify(response_data)
    response.status_code = status_code
    response.headers.extend(headers)
    return response


@blueprint.route('/<string:arxiv_id_str>v<int:arxiv_ver>', methods=['GET'])
def get_relations(arxiv_id_str: str, arxiv_ver: int) -> Response:
    """Get all active (not suppressed or superseded) relations for an e-print."""
    response_data, status_code, headers = \
        controllers.retrieve(arxiv_id_str, arxiv_ver, active_only=True)
    response: Response = jsonify(response_data)
    response.status_code = status_code
    response.headers.extend(headers)
    return response


@blueprint.route('/<string:arxiv_id_str>v<int:arxiv_ver>/log', methods=['GET'])
def get_events(arxiv_id_str: str, arxiv_ver: int) -> Response:
    """Get the complete set of relation events (including suppressed and superseded)."""
    response_data, status_code, headers = \
        controllers.retrieve(arxiv_id_str, arxiv_ver, active_only=False)
    response: Response = jsonify(response_data)
    response.status_code = status_code
    response.headers.extend(headers)
    return response
