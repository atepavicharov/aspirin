import xml.etree.ElementTree as ET
from simple_ddl_parser import parse_from_file

# Inputs
print('Path to file must be with backslashes \\ and no quotes')
ddl_file = input("path to ddl:")
print("Supported dialects are listed here https://pypi.org/project/simple-ddl-parser/: 'mssql','mysql'")
print("Example: mssql,mysql")
sql_dialect = input("sql dialect:")

root = ET.Element('schema')


# https://help.talend.com/r/en-US/7.3/open-studio-user-guide/supported-talend-types

def talend_data_type(data_type):
    type = data_type.lower()
    if type in ['int', 'integer']:
        return "id_Integer"
    elif type in ['tinyint', 'short', 'smallint']:
        return "id_Short"
    elif type in ['boolean', 'bool', 'bit']:
        return "id_Boolean"
    elif type == 'byte':
        return "id_Byte"
    elif type in ['char', 'character']:
        return "id_Character"
    elif type in ['date', 'datetime', 'timestamp', 'time']:
        return "id_Date"
    elif type == 'double':
        return "id_Double"
    elif type == 'float':
        return "id_Float"
    elif type in ['decimal', 'bigdecimal', 'money', 'number', 'numeric']:
        return "id_BigDecimal"
    elif type in ['bigint', 'long']:
        return "id_Long"
    elif type in ['string', 'str', 'varchar', 'nvarchar', 'text', 'uniqueidentifier', 'uuid', 'guid', 'hash']:
        return "id_String"
    else:
        raise Exception("Cannot find Talend type mapping for ddl type: " + data_type)


def talend_db_datatype(data_type):
    if data_type.lower() == 'money':
        return "DECIMAL"
    elif data_type.lower() == 'uniqueidentifier':
        return "VARCHAR"
    else:
        return data_type.upper()


def rm_brackets(instr):
    return instr.replace("[", "").replace("]", "").replace(")", "").replace("(", "")


# result = DDLParser(ddl).run(output_mode="mssql", group_by_type=True)
result = parse_from_file(file_path=ddl_file, output_mode=sql_dialect, group_by_type=True)

for columns in result['tables'][0]['columns']:
    column = ET.SubElement(root, 'column')
    column.set('label', str(rm_brackets(columns['name'])))
    column.set('originalDbColumnName', str(rm_brackets(columns['name'])))
    column.set('nullable', 'true')

    if columns['size'] is not None:
        column.set('length', rm_brackets(str(columns['size']).split(",")[0]))
        if "," in rm_brackets(str(columns['size'])):
            column.set('precision', rm_brackets(str(columns['size']).split(",")[1]).strip())
        else:
            column.set('precision', '-1')
    else:
        column.set('length', '-1')
        column.set('precision', '-1')

    if rm_brackets(columns['type']) == 'money':
        column.set('length', '18')
        column.set('precision', '4')

    if rm_brackets(columns['type']) == 'uniqueidentifier':
        column.set('length', '64')
        # https://dev.mysql.com/doc/workbench/en/wb-migration-database-mssql-typemapping.html

    column.set('talendType', talend_data_type(rm_brackets(columns['type'])))
    column.set('type', talend_db_datatype(rm_brackets(columns['type'])))
    # empty :
    column.set('comment', '')
    column.set('default', '')
    column.set('key', 'false')
    if rm_brackets(columns['type']) == 'datetime':
        column.set('pattern', '"yyyy-MM-dd HH:mm:ss.SSS"')
    elif rm_brackets(columns['type']) == 'time':
        column.set('pattern', '"HH:mm:ss.SSS"')
    else:
        column.set('pattern', '')

tree = ET.ElementTree(root)
ET.indent(tree, space="\t", level=0)
# print(ET.tostring(tree.getroot(), encoding='utf8').decode('utf8'))
try:
    tree.write('schema.xml', encoding="utf-8")
    print("'schema.xml' created successfully")
except Exception as err:
    print("Failed to create the schema xml")
    print(err)
