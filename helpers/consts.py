""" Helper constants """

from groups import (
    M3DMAGIC,
    MDATA,
    NAMEDOBJECT,
    NTRIOBJECT,
    POINTARRAY,
    FACEARRAY,
    TEXVERTS,
    MESHMATRIX,
    MSHMATGROUP,
    SMOOTHGROUP,
    KFDATA,
    OBJECTNODETAG,
    NODEHDR,
    M3DVERSION,
    MESHVERSION,
    MATENTRY,
    MASTERSCALE,
    POINTFLAGARRAY,
    # MESHCOLOR,
    MATNAME,
    MATAMBIENT,
    MATDIFFUSE,
    MATSPECULAR,
    MATSHININESS,
    MATSHIN2PCT,
    MATSHIN3PCT,
    MATTRANSPARENCY,
    MATXPFALL,
    MATREFBLUR,
    MATSELFILLUM,
    MATTWOSIDE,
    MATDECAL,
    MATADDITIVE,
    MATSELFILPCT,
    MATWIRE,
    MATSUPERSMP,
    MATWIRESIZE,
    MATFACEMAP,
    MATXPFALLIN,
    MATPHONGSOFT,
    MATWIREABS,
    # MATSHADING,
    MATTEXMAP,
    COLORF,
    COLOR24,
    LINCOLOR24,
    LINCOLORF,
    # INTPERCENTAGE,
    FLOATPERCENTAGE,
    DEFAULTVIEW,
    VIEWTOP,
    VIEWBOTTOM,
    VIEWLEFT,
    VIEWRIGHT,
    VIEWFRONT,
    VIEWBACK,
    VIEWUSER,
    VIEWCAMERA,
    VIEWWINDOW,
)


GROUP_DICT = {
    0x4D4D: M3DMAGIC,
    0x3D3D: MDATA,
    0x4000: NAMEDOBJECT,
    0x4100: NTRIOBJECT,
    0x4110: POINTARRAY,
    0x4120: FACEARRAY,
    0x4140: TEXVERTS,
    0x4160: MESHMATRIX,
    0x4130: MSHMATGROUP,
    0x4150: SMOOTHGROUP,
    0xB000: KFDATA,
    0xB002: OBJECTNODETAG,
    0xB010: NODEHDR,
    0x2: M3DVERSION,
    0x3D3E: MESHVERSION,
    0xAFFF: MATENTRY,
    0x0100: MASTERSCALE,
    0x4111: POINTFLAGARRAY,
    # 0x4165: MESHCOLOR,
    0xA000: MATNAME,
    0xA010: MATAMBIENT,
    0xA020: MATDIFFUSE,
    0xA030: MATSPECULAR,
    0xA040: MATSHININESS,
    0xA041: MATSHIN2PCT,
    0xA042: MATSHIN3PCT,
    0xA050: MATTRANSPARENCY,
    0xA052: MATXPFALL,
    0xA053: MATREFBLUR,
    0xA080: MATSELFILLUM,
    0xA081: MATTWOSIDE,
    0xA082: MATDECAL,
    0xA083: MATADDITIVE,
    0xA084: MATSELFILPCT,
    0xA085: MATWIRE,
    0xA086: MATSUPERSMP,
    0xA087: MATWIRESIZE,
    0xA088: MATFACEMAP,
    0xA08A: MATXPFALLIN,
    0xA08C: MATPHONGSOFT,
    0xA08E: MATWIREABS,
    # 0xA100: MATSHADING,
    0xA200: MATTEXMAP,
    0x10: COLORF,
    0x11: COLOR24,
    0x12: LINCOLOR24,
    0x13: LINCOLORF,
    # 0x30:   INTPERCENTAGE,
    0x31: FLOATPERCENTAGE,
    0x3000: DEFAULTVIEW,
    0x3010: VIEWTOP,
    0x3020: VIEWBOTTOM,
    0x3030: VIEWLEFT,
    0x3040: VIEWRIGHT,
    0x3050: VIEWFRONT,
    0x3060: VIEWBACK,
    0x3070: VIEWUSER,
    0x3080: VIEWCAMERA,
    0x3090: VIEWWINDOW,
}

CONVERTER_LIST = [
    "M3DMAGIC",
    "MDATA",
    "NAMEDOBJECT",
    "NTRIOBJECT",
    "POINTARRAY",
    "FACEARRAY",
    "TEXVERTS",
    "MESHMATRIX",
    "MSHMATGROUP",
    "SMOOTHGROUP",
    "KFDATA",
    "OBJECTNODETAG",
    "NODEHDR",
    "M3DVERSION",
    "MESHVERSION",
    "MATENTRY",
    "MASTERSCALE",
    "POINTFLAGARRAY",
    "MESHCOLOR",
    "MATNAME",
    "MATAMBIENT",
    "MATDIFFUSE",
    "MATSPECULAR",
    "MATSHININESS",
    "MATSHIN2PCT",
    "MATSHIN3PCT",
    "MATTRANSPARENCY",
    "MATXPFALL",
    "MATREFBLUR",
    "MATSELFILLUM",
    "MATTWOSIDE",
    "MATDECAL",
    "MATADDITIVE",
    "MATSELFILPCT",
    "MATWIRE",
    "MATSUPERSMP",
    "MATWIRESIZE",
    "MATFACEMAP",
    "MATXPFALLIN",
    "MATPHONGSOFT",
    "MATWIREABS",
    "MATSHADING",
    "MATTEXMAP",
    "COLORF",
    "COLOR24",
    "LINCOLOR24",
    "LINCOLORF",
    "INTPERCENTAGE",
    "FLOATPERCENTAGE",
    "DEFAULTVIEW",
    "VIEWTOP",
    "VIEWBOTTOM",
    "VIEWLEFT",
    "VIEWRIGHT",
    "VIEWFRONT",
    "VIEWBACK",
    "VIEWUSER",
    "VIEWCAMERA",
    "VIEWWINDOW",
]
