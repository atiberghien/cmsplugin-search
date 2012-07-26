from cms.apphook_pool import apphook_pool
from cms_search.cms_app import HaystackSearchApphook

apphook_pool.register(HaystackSearchApphook)
