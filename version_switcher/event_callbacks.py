from .utils import load_versions_map


def html_builder_inited(app):
    """
    Initializes the versions map for HTML builder.
    This map is used to generate the version switcher on each page.
    It contains a mapping of page names to the versions of the documentation
    that page is part of.
    """
    if app.builder.name != "html":
        return
    app.builder._ow_version_map = load_versions_map()


def update_version_map(app, docname, content):
    """
    This function is executed when the source file is read.
    It adds the current version to the versions map for the current page.
    """
    if app.builder.name != "version_map":
        return
    try:
        if app.config.version not in app.builder.ow_version_map[docname]:
            app.builder.ow_version_map[docname].append(app.config.version)
    except KeyError:
        app.builder.ow_version_map[docname] = [app.config.version]


def set_version_context(app, pagename, templatename, context, doctree):
    """
    This function is executed when the template is rendered.
    It adds the available versions for the current page to the template context.
    """
    if app.builder.name != "html":
        return
    try:
        context["ow_versions"] = app.builder._ow_version_map[pagename]
    except KeyError as error:
        if pagename not in ["404", "genindex", "search"]:
            raise error
    # Canonical URLs:
    # - All versions, including dev, use stable when the page exists there.
    # - Pages absent from stable keep their versioned URLs.
    # - Index pages use directory URLs rather than index.html.
    # - Rebuild all versions to populate the page map before generating HTML.
    version = context["current_ow_version"]
    stable = context["stable_version"]
    if version == stable or stable in context["ow_versions"]:
        version = "stable"
    if pagename == "index":
        path = ""
    elif pagename.endswith("/index"):
        path = pagename[:-5]
    else:
        path = f"{pagename}.html"
    context["canonical_url"] = (
        f'{context["html_baseurl"]}{context["docs_root"]}/{version}/{path}'
    )
