from plugins.evals.app.gui_api import GuiApi

name = 'Evals'
description = 'A plugin to start the DIY ATT&CK Based Evaluations with CALDERA'
address = '/plugin/evals/gui'


async def initialize(app, services):
    app.router.add_static('/evals', 'plugins/evals/static/', append_version=True)

    gui_api = GuiApi(services=services)
    app.router.add_route('GET', '/plugin/evals/gui', gui_api.splash)

    data_svc = services.get('data_svc')
    await data_svc.load_data(directory='plugins/evals/data')
