from aiohttp_jinja2 import template


class GuiApi:

    def __init__(self, services):
        self.auth_svc = services.get('auth_svc')
        self.plugin_svc = services.get('plugin_svc')
        self.data_svc = services.get('data_svc')

    @staticmethod
    def sort_name(name):
        return name.split('.')[0].zfill(3) + '.' + '.'.join(name.split('.')[1:])

    @template('evals.html')
    async def splash(self, request):
        await self.auth_svc.check_permissions(request)
        plugins = [dict(name=getattr(p, 'name'), address=getattr(p, 'address')) for p in self.plugin_svc.get_plugins()]

        eval_full = 'ef93dd1b-809b-4a0b-b686-fef549cabbe4'
        adversary = (await self.data_svc.explode_adversaries(criteria=dict(adversary_id=eval_full)))[0]
        all_steps = []
        for phase, steps in adversary['phases'].items():
            all_steps.extend(steps)
        all_steps = list({v['name']: v for v in all_steps}.values())
        all_steps = sorted(all_steps, key=lambda i: self.sort_name(i['name']))

        return dict(plugins=plugins, adversary=adversary, steps=all_steps)
