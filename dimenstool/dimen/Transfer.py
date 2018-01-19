#!/usr/bin/env python

import os

import sys
import time
from dimenstool.dimen import Type
from dimenstool.dimen import Creator

"""  将dimens.xml文件解析，根据用户设置的 density  cale_density  xdpi 比例创建转换后的xml（默认比例：1 1 160）  """


class Transfer:
    def __init__(self, density, scale_density, xdpi, file_path):
        if density:
            self.density = density
        else:
            self.density = 1

        if scale_density:
            self.scale_density = scale_density
        else:
            self.scale_density = 1

        if xdpi:
            self.xdpi = xdpi
        else:
            self.xdpi = 160

        if file_path:
            self.file_path = file_path
        else:
            self.file_path = None

    def parse_xml(self, path, creator):
        """"  解析xml文件，每一个节点生成一个字典，并存储到列表中  """
        node_list = []
        if path:
            data = creator.parse_string(path)
            element = data.getElementsByTagName(Type.dimen)
            for node in element:
                node_list.append({str(node.getAttribute(Type.name)): str(node.firstChild.data)})
            return node_list

    def generator(self):
        if self.density and self.scale_density and self.xdpi and self.file_path:

            creator = Creator.Creator(self.density, self.scale_density, self.xdpi)

            # 解析xml文件
            node_list = self.parse_xml(self.file_path, creator)

            # 生成xml格式数据
            creator.creat_xml(node_list)

            del node_list
            return creator.get_child_notes()
        else:
            return None
