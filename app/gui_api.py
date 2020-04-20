from aiohttp_jinja2 import template

class EvalsApi:

    def __init__(self, services):
        self.auth_svc = services.get('auth_svc')
        self.plugin_svc = services.get('plugin_svc')
        self.data_svc = services.get('data_svc')
        self.app_svc = services.get('app_svc')

    @staticmethod
    def sort_name(name):
        return name.split('.')[0].zfill(3) + '.' + '.'.join(name.split('.')[1:])

    @template('evals.html')
    async def splash(self, request):

        abilities = [a for a in await self.data_svc.locate('abilities') if await a.which_plugin() == 'evals_caldera']
        adversaries = [a for a in await self.data_svc.locate('adversaries') if await a.which_plugin() == 'evals_caldera']

        return dict(abilities=abilities, adversaries=adversaries)
