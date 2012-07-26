cmsplugin-search
================

Search form plugin (and utils) for Django CMS Search app

Installation
============

You will need to add the ``cmsplugin_search`` (and required dependencies) to the INSTALLED_APPS
setting in the *settings.py* file::

  INSTALLED_APPS = (
    ...
    'haystack',
    'cms_search',
    'cms_search.search_helpers',
    'cmsplugin_search',
     ...
  )
  
Add these settings in the *settings.py* file::

    #Haystask
    HAYSTACK_SITECONF =  'cmsplugin_search.search_sites'
    HAYSTACK_SEARCH_ENGINE = 'whoosh' #for example
    HAYSTACK_WHOOSH_PATH = os.path.join(os.path.dirname(__file__), 'whoosh_index')
    

if you want to use the ``custom_result`` templates tag, you have add ``CUSTOM_HAYSTACK_RESULT_TEMPLATES`` in the *settings.py* file. The tag allow to render results for heterogeneous type of object::

    CUSTOM_HAYSTACK_RESULT_TEMPLATES = (
        ("cms.models.pagemodel.Page", "search/result/cms_page.html"),
        ("zinnia.models.Entry", "search/result/zinnia_page.html"),
    )

and don't forget to load ``extra_haystack_tags`` in your template ;-).

Finally, in the CMS admin, you have to create a page and affect it the Search app hook.

For initiate indexing : ./manage.py rebuild_index --noinput