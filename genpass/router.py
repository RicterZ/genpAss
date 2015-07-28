# coding=utf-8
import generator
from rules import built_in


field_map = (
    ('qq', None),
    ('birthday', built_in.date_formats),
    ('company', built_in.general_formats),
    ('name', built_in.name_formats, generator.generate_name),
    (('username', 'name'), built_in.general_formats),
    (('email', 'name'), built_in.general_formats),
)
