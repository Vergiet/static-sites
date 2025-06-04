
ITALIC_REGEX = r"(?P<begin>.*)(?P<midden>_.+_)(?P<eind>.*)"
CODE_REGEX = r"(?P<begin>.*)(?P<midden>`.+`)(?P<eind>.*)"
BOLD_REGEX = r"(?P<begin>.*)(?P<midden>\*\*.+\*\*)(?P<eind>.*)"
LINK_REGEX_FULL = r"(?P<begin>[^\n\r\[\]]*)(?P<midden>\[[^\n\r\[\]\(\)]*\].?\([^\n\r\[\]\(\)]*\))(?P<einde>[^\n\r\[\]]*)"
IMG_REGEX_FULL = r"(?P<begin>[^\n\r\[\]]*)(?P<midden>!\[[^\n\r\[\]\(\)]*\].?\([^\n\r\[\]\(\)]*\))(?P<einde>[^!\n\r\[\]]*)"
URL_REGEX_SPLIT = r"\[(?P<alt_text>[\w\s\d]*)\]\((?P<url>[^()]*)\)"

# https://regex101.com/r/vNLANm/1