from django.shortcuts import get_object_or_404
from django.conf import settings
import requests
from qm.models import Query

PROXY = settings.PROXY

def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]

def run():
    url = 'https://lolrmm.io/api/rmm_tools.json'
    r = requests.get(url, verify=False, proxies=PROXY)

    domains = []
    for item in r.json():
        if 'Domains' in item and item['Domains']:
            for d in item['Domains']:
                if d.strip():
                    domains.append(d.strip())

    # Remove duplicates
    domains = list(set(domains))

    # Build S1QL in chunks
    chunk_size = 100
    domain_chunks = list(split(domains, chunk_size))
    s1ql_list = []
    for chunk in domain_chunks:
        s1ql_list.append("event.dns.request contains:anycase ({})".format(
            ', '.join(["'{}'".format(d) for d in chunk])
        ))

    s1ql = '\n  or '.join(s1ql_list)

    dynamic_query = """event.type = 'DNS Resolved'
    and (
      {}
    )""".format(s1ql)

    query = get_object_or_404(Query, name='lolrmm_related_domains')
    query.query = dynamic_query
    query.save()