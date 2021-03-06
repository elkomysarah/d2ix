import logging

logger = logging.getLogger(__name__)


def process_lvl_spatial(_data):
    df = _data['base_input']['lvl_spatial'].copy()
    lvl_spatial = []
    for index, row in df.iterrows():
        lvl_spatial.append([row['region'], row['sub_region']])

    data = {'lvl_spatial': lvl_spatial}

    logger.debug('Created helper data structure: \'lvl_spatial\'')
    return data['lvl_spatial']
