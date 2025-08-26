# Openint

Types:

```python
from openint.types import (
    Connector,
    Integration,
    AssignConnectionResponse,
    CheckConnectionResponse,
    CreateConnectionResponse,
    CreateConnnectorConfigResponse,
    CreateTokenResponse,
    DeleteAssignmentResponse,
    DeleteConnectionResponse,
    DeleteConnectorConfigResponse,
    GetConectorConfigResponse,
    GetConnectionResponse,
    GetCurrentUserResponse,
    ListAssignmentsResponse,
    ListConnectionConfigsResponse,
    ListConnectionsResponse,
    ListConnectorsResponse,
    ListConnnectorConfigsResponse,
    ListCustomersResponse,
    ListEventsResponse,
    UpsertConnnectorConfigResponse,
    UpsertCustomerResponse,
)
```

Methods:

- <code title="put /v2/connection/{id}/assignment/{replId}">client.<a href="./src/openint/_client.py">assign_connection</a>(repl_id, \*, id) -> <a href="./src/openint/types/assign_connection_response.py">AssignConnectionResponse</a></code>
- <code title="post /v1/connection/{id}/check">client.<a href="./src/openint/_client.py">check_connection</a>(id) -> <a href="./src/openint/types/check_connection_response.py">CheckConnectionResponse</a></code>
- <code title="post /v2/connection">client.<a href="./src/openint/_client.py">create_connection</a>(\*\*<a href="src/openint/types/client_create_connection_params.py">params</a>) -> <a href="./src/openint/types/create_connection_response.py">CreateConnectionResponse</a></code>
- <code title="post /v2/connector-config">client.<a href="./src/openint/_client.py">create_connnector_config</a>(\*\*<a href="src/openint/types/client_create_connnector_config_params.py">params</a>) -> <a href="./src/openint/types/create_connnector_config_response.py">CreateConnnectorConfigResponse</a></code>
- <code title="post /v1/customer/{customer_id}/token">client.<a href="./src/openint/_client.py">create_token</a>(customer_id, \*\*<a href="src/openint/types/client_create_token_params.py">params</a>) -> <a href="./src/openint/types/create_token_response.py">CreateTokenResponse</a></code>
- <code title="delete /v2/connection/{id}/assignment/{replId}">client.<a href="./src/openint/_client.py">delete_assignment</a>(repl_id, \*, id) -> <a href="./src/openint/types/delete_assignment_response.py">DeleteAssignmentResponse</a></code>
- <code title="delete /v2/connection/{id}">client.<a href="./src/openint/_client.py">delete_connection</a>(id) -> <a href="./src/openint/types/delete_connection_response.py">DeleteConnectionResponse</a></code>
- <code title="delete /v2/connector-config/{id}">client.<a href="./src/openint/_client.py">delete_connector_config</a>(id) -> <a href="./src/openint/types/delete_connector_config_response.py">DeleteConnectorConfigResponse</a></code>
- <code title="get /v2/connector-config/{id}">client.<a href="./src/openint/_client.py">get_conector_config</a>(id, \*\*<a href="src/openint/types/client_get_conector_config_params.py">params</a>) -> <a href="./src/openint/types/get_conector_config_response.py">GetConectorConfigResponse</a></code>
- <code title="get /v2/connection/{id}">client.<a href="./src/openint/_client.py">get_connection</a>(id, \*\*<a href="src/openint/types/client_get_connection_params.py">params</a>) -> <a href="./src/openint/types/get_connection_response.py">GetConnectionResponse</a></code>
- <code title="get /v1/viewer">client.<a href="./src/openint/_client.py">get_current_user</a>() -> <a href="./src/openint/types/get_current_user_response.py">GetCurrentUserResponse</a></code>
- <code title="get /v2/connection/{id}/assignment">client.<a href="./src/openint/_client.py">list_assignments</a>(id) -> <a href="./src/openint/types/list_assignments_response.py">ListAssignmentsResponse</a></code>
- <code title="get /v2/connector-config">client.<a href="./src/openint/_client.py">list_connection_configs</a>(\*\*<a href="src/openint/types/client_list_connection_configs_params.py">params</a>) -> <a href="./src/openint/types/list_connection_configs_response.py">SyncOffsetPagination[ListConnectionConfigsResponse]</a></code>
- <code title="get /v2/connection">client.<a href="./src/openint/_client.py">list_connections</a>(\*\*<a href="src/openint/types/client_list_connections_params.py">params</a>) -> <a href="./src/openint/types/list_connections_response.py">SyncOffsetPagination[ListConnectionsResponse]</a></code>
- <code title="get /v2/connector">client.<a href="./src/openint/_client.py">list_connectors</a>(\*\*<a href="src/openint/types/client_list_connectors_params.py">params</a>) -> <a href="./src/openint/types/list_connectors_response.py">SyncOffsetPagination[ListConnectorsResponse]</a></code>
- <code title="get /v2/connector-config">client.<a href="./src/openint/_client.py">list_connnector_configs</a>(\*\*<a href="src/openint/types/client_list_connnector_configs_params.py">params</a>) -> <a href="./src/openint/types/list_connnector_configs_response.py">SyncOffsetPagination[ListConnnectorConfigsResponse]</a></code>
- <code title="get /v1/customer">client.<a href="./src/openint/_client.py">list_customers</a>(\*\*<a href="src/openint/types/client_list_customers_params.py">params</a>) -> <a href="./src/openint/types/list_customers_response.py">SyncOffsetPagination[ListCustomersResponse]</a></code>
- <code title="get /v1/event">client.<a href="./src/openint/_client.py">list_events</a>(\*\*<a href="src/openint/types/client_list_events_params.py">params</a>) -> <a href="./src/openint/types/list_events_response.py">SyncOffsetPagination[ListEventsResponse]</a></code>
- <code title="put /v2/connector-config/{id}">client.<a href="./src/openint/_client.py">upsert_connnector_config</a>(id, \*\*<a href="src/openint/types/client_upsert_connnector_config_params.py">params</a>) -> <a href="./src/openint/types/upsert_connnector_config_response.py">UpsertConnnectorConfigResponse</a></code>
- <code title="put /v1/customer">client.<a href="./src/openint/_client.py">upsert_customer</a>(\*\*<a href="src/openint/types/client_upsert_customer_params.py">params</a>) -> <a href="./src/openint/types/upsert_customer_response.py">UpsertCustomerResponse</a></code>
