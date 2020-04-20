from plugins.evals_caldera.app.gui_api import EvalsApi
from app.utility.base_world import BaseWorld

name = 'Evals_Caldera'
description = 'A plugin to start the DIY ATT&CK Based Evaluations with CALDERA'
address = '/plugin/evals/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    app.router.add_static('/evals', 'plugins/evals_caldera/static/', append_version=True)

    evals_api = EvalsApi(services=services)
    app.router.add_route('GET', '/plugin/evals/gui', evals_api.splash)
