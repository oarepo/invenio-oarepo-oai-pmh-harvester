from oarepo_oai_pmh_harvester.proxies import current_oai_client
from oarepo_oai_pmh_harvester.transformer import OAITransformer


def rule(provider, parser, path, phase=OAITransformer.PHASE_PRE):
    def wrapper(func):
        current_oai_client.add_rule(func, provider, parser, path, phase)

    return wrapper


def parser(name):
    def wrapper(func):
        current_oai_client.add_parser(func, name)

    return wrapper