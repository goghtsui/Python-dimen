#!/usr/bin/env python

from dimenstool.dimen import Type

"""   将dimens中数值根据对应的 density 和 dp、px 等单位 转换为相应值 """


def format_value(value, density, scale_density, xdpi):
    """  截取字符串中的数字, 单位，并做对应转换  """
    if Type.dip in value:
        unit = value[-3:]
        number = str(value[:-3])
        result = switch(unit, number, density, scale_density, xdpi)
        return str(result) + unit
    elif Type.px in value or Type.dp in value or Type.sp in value or Type.pt in value or Type.inch in value or Type.mm in value:
        unit = value[-2:]
        number = str(value[:-2])
        result = switch(unit, number, density, scale_density, xdpi)
        return str(result) + unit
    else:
        if value.isdigit():
            return str(value)


def switch(unit, value, density, scale_density, xdpi):
    """ 根据对应的单位，对数值做不同的值转换 """
    switcher = {
        Type.px: value,
        Type.dp: float(value) * float(density),
        Type.dip: float(value) * float(density),
        Type.sp: float(value) * float(scale_density),
        Type.pt: float(value) * float(xdpi) * (1.0 / 72.0),
        Type.inch: float(value) * float(xdpi),
        Type.mm: float(value) * float(xdpi) * (1.0 / 25.4),
    }

    return switcher.get(unit, 0)
