import os

from dotenv import load_dotenv

load_dotenv('.env')

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', None)
OPENAI_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-4o-2024-11-20')
OPENAI_EMBEDDING_MODEL = os.environ.get('OPENAI_EMBEDDING_MODEL', 'text-embedding-ada-002')

MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '1234')
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_PORT = os.environ.get('MYSQL_PORT', '3306')
MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME', 'chicago_search_api')

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDISH_TTL = os.environ.get('REDISH_TTL', 432000)

NOTIFICATION_MANAGER_WS = os.environ.get('NOTIFICATION_MANAGER_WS',
                                         'ws://chicago-notifications.datafabdevelopment.com/v1')
NOTIFICATION_MANAGER_URL = os.environ.get('NOTIFICATION_MANAGER_URL',
                                          'https://chicago-notifications.datafabdevelopment.com/v1')

USER_MANAGER_URL = os.environ.get('USER_MANAGER_URL', 'https://chicago-um.datafabdevelopment.com/api/v1/')

ENTITY_MANAGER_URL = os.environ.get('ENTITY_MANAGER_URL', 'http://100.78.163.53:1032/v1/')
SOURCE_MANAGER_URL = os.environ.get('SOURCE_MANAGER_URL', 'https://chicago-sm.datafabdevelopment.com/v1/')
SCHEMA_BUILDER_URL = os.environ.get('SCHEMA_BUILDER_URL', 'https://chicago-schema-builder.datafabdevelopment.com/v1/')
GRAPH_SERVICE_URL = os.environ.get('GRAPH_SERVICE_URL', 'https://chicago-graph.datafabdevelopment.com/v1/')
OPPORTUNITY_MANAGEMENT_URL = os.environ.get('OPPORTUNITY_MANAGEMENT_URL', 'https://chicago-op.datafabdevelopment.com/v1/')
DOCUMENT_UNDERSTANDING_URL = os.environ.get('DOCUMENT_UNDERSTANDING_URL', 'https://document-understanding.datafabdevelopment.com/v1/')
DOCUMENT_MANAGEMENT_SERVICE_URL = os.environ.get('DOCUMENT_MANAGEMENT_SERVICE_URL', 'https://chicago-dms.datafabdevelopment.com/v1/')
TRANSLATOR_SERVICE = os.environ.get('TRANSLATOR_SERVICE', 'https://chicago-translation-dev.datafabdevelopment.com/v1/')
QUESTION_AND_BUILDER_SERVICE = os.environ.get('QUESTION_AND_BUILDER_SERVICE', 'https://chicago-qb.datafabdevelopment.com/v1/')
N8N_WORKFLOW_MANAGER_URL = os.environ.get('N8N_WORKFLOW_MANAGER_URL', 'https://chicago-workflow-dev.datafabdevelopment.com/api/v1/')
OPEN_METADATA_SERVICE_URL = os.environ.get('OPEN_METADATA_SERVICE_URL', 'https://chicago-dev-open-meta.datafabdevelopment.com/api/v1/')
LIST_MANAGEMENT_SERVICE_URL = os.environ.get('LIST_MANAGEMENT_SERVICE_URL', 'https://chicago-lm-dev.datafabdevelopment.com/v1/')
N8N_WEBHOOK_URL = os.environ.get('N8N_WEBHOOK_URL', 'https://chicago-workflow-dev.datafabdevelopment.com/webhook/')

# brandfetch
BRANDFETCH_CLIENT_ID = os.environ.get('BRANDFETCH_CLIENT_ID', '')
BRANDFETCH_BASE_URL = os.environ.get('BRANDFETCH_BASE_URL', 'https://api.brandfetch.io/v2/')
BRANDFETCH_API_KEY = os.environ.get('BRANDFETCH_API_KEY', '')

OPEN_METADATA_ADMIN_EMAIL = os.environ.get('OPEN_METADATA_ADMIN_EMAIL', '')
OPEN_METADATA_ADMIN_PASSWORD = os.environ.get('OPEN_METADATA_ADMIN_PASSWORD', '')

N8N_API_KEY = os.environ.get('N8N_API_KEY', '')

# N8N workflow ids
ADD_OPPORTUNITY_CONTAINED_ITEMS_WORKFLOW_ID = os.environ.get('ADD_OPPORTUNITY_CONTAINED_ITEMS_WORKFLOW_ID', 'ca2347bd-01b7-4aee-9f54-4432aceee7a1')
ADD_OPPORTUNITY_CONTAINED_ITEMS_SUMMARY_WORKFLOW_ID = os.environ.get('ADD_OPPORTUNITY_CONTAINED_ITEMS_SUMMARY_WORKFLOW_ID', '0318e387-bd33-4e79-bcbd-1b6b3e017152')
PAST_DOCUMENT_CREATION_WORKFLOW_ID = os.environ.get('PAST_DOCUMENT_CREATION_WORKFLOW_ID', 'a768fb9d-afcb-4c73-b030-1c602ace22d8')

# replaceable urls
SELF_SERVICE_URL = os.environ.get('SELF_SERVICE_URL', 'https://chicago-chat.datafabdevelopment.com/v1/')
ENTITY_MANAGER_DNS_URL = os.environ.get('ENTITY_MANAGER_DNS_URL', 'https://chicago-entity.datafabdevelopment.com/v1/')

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
SQL_LOG = os.environ.get('SQL_LOG', 'False')
WEB_SOCKET_LOG = os.environ.get('WEB_SOCKET_LOG', 'True')
