def setup(app):
    from .builders import VersionSwitcherIndexBuilder
    from .event_callbacks import (
        html_builder_inited,
        update_version_map,
        set_version_context,
    )

    app.add_builder(VersionSwitcherIndexBuilder)
    app.connect('builder-inited', html_builder_inited)
    app.connect('source-read', update_version_map)
    app.connect('html-page-context', set_version_context)
    return {
        'version': '0.0.1a',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
