import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources


@dlt.source(name="feegow_agenda")
def feegow_source(feegow_token=dlt.secrets["sources.feegow_agenda.feegow_token"]):

    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.feegow.com/v1/api/",
            "headers": {
                "X-Access-Token": feegow_token,
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        },
        "resource_defaults": {
            "endpoint": {
                "method": "GET",
                "response_actions": [{"status_code": 404, "action": "ignore"}]
            }
        },
        "resources": [
            {
                "name": "agendamentos",
                "write_disposition": {
                    "disposition": "merge",
                    "strategy": "scd2"
                },
                "primary_key": ["agendamento_id"],
                "endpoint": {
                    "path": "appoints/search",
                    "params": {
                        "data_start": "2025-06-09",
                        "data_end": "2025-06-13"
                    },
                    "data_selector": "content"
                },
            },
            {
                "name": "status",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["id"],
                "endpoint": {
                    "path": "appoints/status",
                    "data_selector": "content"
                }
            },
            {
                "name": "motivos",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["id"],
                "endpoint": {
                    "path": "appoints/motives",
                    "data_selector": "content"
                }
            },
            {
                "name": "canais",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["id"],
                "endpoint": {
                    "path": "appoints/list-channel",
                    "data_selector": "content"
                }
            },
            {
                "name": "pacientes",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["patient_id"],
                "endpoint": {
                    "path": "patient/list",
                    "data_selector": "content"
                }
            },
            {
                "name": "procedimentos",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["procedimento_id"],
                "endpoint": {
                    "path": "procedures/list",
                    "data_selector": "content"
                }
            },
            {
                "name": "profissionais",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["profissional_id"],
                "endpoint": {
                    "path": "professional/list",
                    "data_selector": "content"
                }
            },
            {
                "name": "locais",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["id"],
                "endpoint": {
                    "path": "company/list-local",
                    "data_selector": "content"
                }
            },
            {
                "name": "convenios",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["convenio_id"],
                "endpoint": {
                    "path": "insurance/list",
                    "data_selector": "content"
                }
            },
            {
                "name": "unidades",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["unidade_id"],
                "endpoint": {
                    "path": "company/list-unity",
                    "data_selector": "content.unidades"
                }
            },
            {
                "name": "matriz",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["unidade_id"],
                "endpoint": {
                    "path": "company/list-unity",
                    "data_selector": "content.matriz"
                }
            },
            {
                "name": "especialidades",
                "write_disposition": {
                    "disposition": "replace"
                },
                "primary_key": ["especialidade_id"],
                "endpoint": {
                    "path": "specialties/list",
                    "data_selector": "content"
                }
            }


        ]
    }

    yield from rest_api_resources(config)
