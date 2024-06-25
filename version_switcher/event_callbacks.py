from .utils import load_versions_map


def html_builder_inited(app):
    if app.builder.name != 'html':
        return
    app.builder._ow_version_map = load_versions_map()


def update_version_map(app, docname, content):
    try:
        app.builder.ow_version_map[docname].append(app.config.version)
    except KeyError:
        app.builder.ow_version_map[docname] = [app.config.version]


def set_version_context(app, pagename, templatename, context, doctree):
    try:
        context['ow_versions'] = app.builder._ow_version_map[pagename]
    except KeyError as error:
        if pagename not in ['404', 'genindex', 'search']:
            raise error
