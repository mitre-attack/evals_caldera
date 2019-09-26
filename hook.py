from plugins.evals_caldera.app.gui_api import EvalsApi

name = 'Evals_Caldera'
description = 'A plugin to start the DIY ATT&CK Based Evaluations with CALDERA'
address = '/plugin/evals/gui'


async def initialize(app, services):
    app.router.add_static('/evals', 'plugins/evals_caldera/static/', append_version=True)

    evals_api = EvalsApi(services=services)
    app.router.add_route('GET', '/plugin/evals/gui', evals_api.splash)

    data_svc = services.get('data_svc')
    await data_svc.load_data(directory='plugins/evals_caldera/data')
