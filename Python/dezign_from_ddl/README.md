1. Create an "empty" DeZign file with the db type and version
2. Replace the content enclosed by the <ENTITIES> tag
```xml
<DOMAINS>
</DOMAINS>

<ENTITIES> <-- REPLACE FROM HERE (incl.)
...
</ENTITIES> <-- REPLACE TO HERE (incl.)

<SUBCATEGORIES>
</SUBCATEGORIES>
```

The script is using [simple_ddl_parser](https://pypi.org/project/simple-ddl-parser/) which should pick the target SQL dialect.