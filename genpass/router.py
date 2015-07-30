# coding=utf-8
import generator
from rules import built_in


field_map = (
    ('qq', None),
    ('birthday', built_in.date_formats),
    ('company', built_in.general_formats),
    ('name', built_in.name_formats, generator.generate_name),
    ('username', built_in.general_formats),
    (('email', 'username'), built_in.general_formats, generator.generate_id_string),
)
