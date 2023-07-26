import textwrap

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(url="https://hub.snapshot.org/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)


def query_snapshot_proposal(proposal_id):
    return client.execute(gql(textwrap.dedent(f"""\
        query {{
            proposal(id:"{proposal_id}") {{
                id
                title
                body
                choices
                start
                end
                snapshot
                state
                author
                created
                scores
                scores_by_strategy
                scores_total
                scores_updated
                plugins
                network
                strategies {{
                    name
                    network
                    params
                }}
                space {{
                    id
                    name
                }}
            }}
        }}
    """)))


def query_snapshot_space(space_id):
    return client.execute(gql(textwrap.dedent(f"""\
        query Spaces {{
            spaces(where: {{id: "{space_id}"}}) {{
                id
                name
                about
                network
                symbol
                strategies {{
                    name
                    network
                    params
                }}
                admins
                moderators
                members
                filters {{
                    minScore
                    onlyMembers
                }}
                plugins
            }}
        }}
    """)))
