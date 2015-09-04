# coding: utf-8
import genpass.generator
from genpass.rules import built_in


BUILT_IN_FIELD_MAP = (
    ('qq', None),
    ('birthday', built_in.date_formats),
    ('company', built_in.general_formats),
    ('name', built_in.name_formats, genpass.generator.generate_name),
    ('username', built_in.general_formats),
    (('email', 'username'), built_in.general_formats, genpass.generator.generate_id_string),
)

SEQUENCES = (tuple, list, set)