import re


END_PUNCTUATION = r"[\.\?>\"'\)!,}:;\u201d\u2019\uff1e\uff1c\]]*"

SEPARATOR_DEFANGS = r"[\(\)\[\]{}<>\\]"

URL_SPLIT_STR = r"[>\"'\),};]"

GENERIC_URL = re.compile(r"""
        (
            [fhstu]\S\S?[px]s?
            (?:
                :\/\/|
                :\\\\|
                :?__
            )
            (?:
                \x20|
                """ + SEPARATOR_DEFANGS + r"""
            )*
            \w
            \S+?
            (?:\x20[\/\.][^\.\/\s]\S*?)*
        )
    """ + END_PUNCTUATION + r"""
        (?=\s|$)
    """, re.IGNORECASE | re.VERBOSE | re.UNICODE)

BRACKET_URL = re.compile(r"""
        \b
        (
            [\.\:\/\\\w\[\]\(\)-]+
            (?:
                \x20?
                [\(\[]
                \x20?
                \.
                \x20?
                [\]\)]
                \x20?
                \S*?
            )+
        )
    """ + END_PUNCTUATION + r"""
        (?=\s|$)
    """, re.VERBOSE | re.UNICODE)

BACKSLASH_URL = re.compile(r"""
        \b
        (
            [\:\/\\\w\[\]\(\)-]+
            (?:
                \x20?
                \\?\.
                \x20?
                \S*?
            )*?
            (?:
                \x20?
                \\\.
                \x20?
                \S*?
            )
            (?:
                \x20?
                \\?\.
                \x20?
                \S*?
            )*
        )
    """ + END_PUNCTUATION + r"""
        (?=\s|$)
    """, re.VERBOSE | re.UNICODE)

HEXENCODED_URL = re.compile(r"""
        (
            [46][86]
            (?:[57]4)?
            [57]4[57]0
            (?:[57]3)?
            3a2f2f
            (?:2[356def]|3[0-9adf]|[46][0-9a-f]|[57][0-9af])+
        )
        (?:[046]0|2[0-2489a-c]|3[bce]|[57][b-e]|[8-f][0-9a-f]|0a|0d|09|[
            \x5b-\x5d\x7b\x7d\x0a\x0d\x20
        ]|$)
    """, re.IGNORECASE | re.VERBOSE)

URLENCODED_URL = re.compile(r"""
        (s?[hf]t?tps?%3A%2F%2F\w[\w%-]*?)(?:[^\w%-]|$)
    """, re.IGNORECASE | re.VERBOSE)

B64ENCODED_URL = re.compile(r"""
        (
            (?:
                [\x2b\x2f-\x39A-Za-z]\s*[\x2b\x2f-\x39A-Za-z]\s*[\x31\x35\x39BFJNRVZdhlptx]\s*[Gm]\s*[Vd]\s*[FH]\s*[A]\s*\x36\s*L\s*y\s*[\x2b\x2f\x38-\x39]\s*|
                [\x2b\x2f-\x39A-Za-z]\s*[\x2b\x2f-\x39A-Za-z]\s*[\x31\x35\x39BFJNRVZdhlptx]\s*[Io]\s*[Vd]\s*[FH]\s*[R]\s*[Qw]\s*[O]\s*i\s*\x38\s*v\s*[\x2b\x2f-\x39A-Za-z]\s*|
                [\x2b\x2f-\x39A-Za-z]\s*[\x2b\x2f-\x39A-Za-z]\s*[\x31\x35\x39BFJNRVZdhlptx]\s*[Io]\s*[Vd]\s*[FH]\s*[R]\s*[Qw]\s*[Uc]\s*[z]\s*o\s*v\s*L\s*[\x2b\x2f-\x39w-z]\s*|
                [\x2b\x2f-\x39A-Za-z]\s*[\x30\x32EGUWkm]\s*[Z]\s*[\x30U]\s*[Uc]\s*[D]\s*o\s*v\s*L\s*[\x2b\x2f-\x39w-z]\s*|
                [\x2b\x2f-\x39A-Za-z]\s*[\x30\x32EGUWkm]\s*[h]\s*[\x30U]\s*[Vd]\s*[FH]\s*[A]\s*\x36\s*L\s*y\s*[\x2b\x2f\x38-\x39]\s*|
                [\x2b\x2f-\x39A-Za-z]\s*[\x30\x32EGUWkm]\s*[h]\s*[\x30U]\s*[Vd]\s*[FH]\s*[B]\s*[Tz]\s*[O]\s*i\s*\x38\s*v\s*[\x2b\x2f-\x39A-Za-z]\s*|
                [RZ]\s*[ln]\s*[R]\s*[Qw]\s*[O]\s*i\s*\x38\s*v\s*[\x2b\x2f-\x39A-Za-z]\s*|
                [Sa]\s*[FH]\s*[R]\s*[\x30U]\s*[Uc]\s*[D]\s*o\s*v\s*L\s*[\x2b\x2f-\x39w-z]\s*|
                [Sa]\s*[FH]\s*[R]\s*[\x30U]\s*[Uc]\s*[FH]\s*[M]\s*\x36\s*L\s*y\s*[\x2b\x2f\x38-\x39]\s*
            )
            [A-Za-z0-9+/=\s]{1,357}
        )
        (?=[^A-Za-z0-9+/=\s]|$)
    """, re.VERBOSE)

IPV4 = re.compile(r"""
        (?:^|
            (?![^\d\.])
        )
        (?:
            (?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])
            [\[\(\\]*?\.[\]\)]*?
        ){3}
        (?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])
        (?:(?=[^\d\.])|$)
    """, re.VERBOSE)

IPV6 = re.compile(r"""
        \b(?:[a-f0-9]{1,4}:|:){2,7}(?:[a-f0-9]{1,4}|:)\b
    """, re.IGNORECASE | re.VERBOSE)

EMAIL = re.compile(r"""
        (
            [a-z0-9_.+-]+
            [\(\[{\x20]*
            (?:@|\Wat\W)
            [\)\]}\x20]*
            [a-z0-9-]+
            (?:
                (?:
                    (?:
                        \x20*
                        """ + SEPARATOR_DEFANGS + r"""
                        \x20*
                    )*
                    \.
                    (?:
                        \x20*
                        """ + SEPARATOR_DEFANGS + r"""
                        \x20*
                    )*
                    |
                    \W+dot\W+
                )
                [a-z0-9-]+?
            )+
        )
    """ + END_PUNCTUATION + r"""
        (?=\s|$)
    """, re.IGNORECASE | re.VERBOSE | re.UNICODE)

MD5 = re.compile(r"(?:[^a-fA-F\d]|\b)([a-fA-F\d]{32})(?:[^a-fA-F\d]|\b)")
SHA1 = re.compile(r"(?:[^a-fA-F\d]|\b)([a-fA-F\d]{40})(?:[^a-fA-F\d]|\b)")
SHA256 = re.compile(r"(?:[^a-fA-F\d]|\b)([a-fA-F\d]{64})(?:[^a-fA-F\d]|\b)")
SHA512 = re.compile(
    r"(?:[^a-fA-F\d]|\b)([a-fA-F\d]{128})(?:[^a-fA-F\d]|\b)")

YARA_PARSE = re.compile(r"""
        (?:^|\s)
        (
            (?:
                \s*?import\s+?"[^\r\n]*?[\r\n]+|
                \s*?include\s+?"[^\r\n]*?[\r\n]+|
                \s*?//[^\r\n]*[\r\n]+|
                \s*?/\*.*?\*/\s*?
            )*
            (?:
                \s*?private\s+|
                \s*?global\s+
            )*
            rule\s*?
            \w+\s*?
            (?:
                :[\s\w]+
            )?
            \s+\{
            .*?
            condition\s*?:
            .*?
            \s*\}
        )
        (?:$|\s)
    """, re.MULTILINE | re.DOTALL | re.VERBOSE)

CREDIT_CARD = re.compile(r"[0-9]{4}[ ]?[-]?[0-9]{4}[ ]?[-]?[0-9]{4}[ ]?[-]?[0-9]{4}")

rintels = [(GENERIC_URL, "GENERIC_URL"),
           (BRACKET_URL, "BRACKET_URL"),
           (BACKSLASH_URL, "BACKSLASH_URL"),
           (HEXENCODED_URL, "HEXENCODED_URL"),
           (URLENCODED_URL, "URLENCODED_URL"),
           (B64ENCODED_URL, "B64ENCODED_URL"),
           (IPV4, "IPV4"),
           (IPV6, "IPV6"),
           (EMAIL, "EMAIL"),
           (MD5, "MD5"),
           (SHA1, "SHA1"),
           (SHA256, "SHA256"),
           (SHA512, "SHA512"),
           (YARA_PARSE, "YARA_PARSE"),
           (CREDIT_CARD, "CREDIT_CARD")]


rscript = re.compile(r'<(script|SCRIPT).*(src|SRC)=([^\s>]+)')
rhref = re.compile(r'<[aA].*(href|HREF)=([^\s>]+)')
rendpoint = re.compile(r'[\'"](/.*?)[\'"]|[\'"](http.*?)[\'"]')
rentropy = re.compile(r'[\w-]{16,45}')
