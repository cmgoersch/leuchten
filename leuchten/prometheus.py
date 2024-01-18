from prometheus_api_client import PrometheusConnect

from leuchten.config import settings

prom = PrometheusConnect(url=settings.prometheus_host)


def get_host_icmp_status():
    return prom.custom_query(query='')
