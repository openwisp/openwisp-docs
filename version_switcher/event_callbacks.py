from .utils import load_versions_map


def html_builder_inited(app):
    """
    Initializes the versions map for HTML builder.
    This map is used to generate the version switcher on each page.
    It contains a mapping of page names to the versions of the documentation
    that page is part of.
    """
    if app.builder.name != 'html':
        return
    app.builder._ow_version_map = load_versions_map()


def update_version_map(app, docname, content):
    """
    This function is executed when the source file is read.
    It adds the current version to the versions map for the current page.
    """
    if app.builder.name != 'ow_dummy':
        return
    try:
        app.builder.ow_version_map[docname].append(app.config.version)
    except KeyError:
        app.builder.ow_version_map[docname] = [app.config.version]


def set_version_context(app, pagename, templatename, context, doctree):
    """
    This function is executed when the template is rendered.
    It adds the available versions for the current page to the template context.
    """
    if app.builder.name != 'html':
        return
    try:
        context['ow_versions'] = app.builder._ow_version_map[pagename]
    except KeyError as error:
        if pagename not in ['404', 'genindex', 'search']:
            raise error
